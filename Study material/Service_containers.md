# Service containers

**What they are.** Extra Docker containers Actions starts **for one job** (database, cache, broker). Pulled and started before the steps, destroyed when the job ends. Per-job, never shared across jobs or runs, no automatic restart if one crashes mid-job.

**Hard requirement.** Linux + Docker: `ubuntu-latest` or a Linux self-hosted runner with Docker installed. No macOS (no Docker daemon), no Windows (no Linux containers). Same rule as Docker container actions.

## The one question that decides everything: where do the steps run?

| Job runs… | Address | Port | `ports:` needed? |
|---|---|---|---|
| in a container (`container:` set) | service **label** as hostname | **container** port | no |
| on the runner host (no `container:`) | `localhost` | mapped **host** port | yes |

## Mode 1 — job in a container: label + container port

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    container: node:20          # <- THIS line puts the steps in a container
    services:
      postgres:                 # <- label = hostname on the shared network
        image: postgres:16
        env:
          POSTGRES_PASSWORD: ci
        # no ports: needed — same Docker network, container port reachable directly
    steps:
      - uses: actions/checkout@v4
      - run: npm test
        env:
          DATABASE_URL: postgres://postgres:ci@postgres:5432/postgres
          #                       hostname ----^^^^^^^^  ^^^^-- container port
```

Job container and service containers sit on the same Docker bridge network; Docker's DNS resolves each **label** to the service's IP. Use the port the service listens on **inside its container**; nothing is published to the host.

## Mode 2 — job on the host: localhost + mapped host port

```yaml
jobs:
  test:
    runs-on: ubuntu-latest      # no container: -> steps run directly on the VM
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: ci
        ports:
          - 5432:5432           # <- REQUIRED now: host port : container port
    steps:
      - uses: actions/checkout@v4
      - run: npm test
        env:
          DATABASE_URL: postgres://postgres:ci@localhost:5432/postgres
          #                        hostname ---^^^^^^^^^  ^^^^-- HOST port
```

The runner VM is **not** on the Docker network, so labels resolve to nothing. The only doorway is a published port: connect to `localhost:<host-port>`. With `"8080:5432"` the steps connect to `localhost:8080` (host port left, container port right).

## The cross-check (exam trap in both directions)

- Mode 1 with `localhost:5432` → **connection refused** (nothing listens on the job container's own localhost).
- Mode 2 with `postgres:5432` → **hostname not found** (`getaddrinfo ENOTFOUND postgres` — host isn't on the Docker network).

First thing to look for in any question: **is `container:` present on the job?** That single line decides hostname, port, and whether `ports:` is required.

## Random host ports + discovery

`ports: ["6379/tcp"]` (or bare `6379`) = Docker picks a random free host port. Discover it from the **`job` context**:

```yaml
env:
  REDIS_PORT: ${{ job.services.redis.ports[6379] }}
```

`job.services.<label>.ports` is a map: key = container port, value = assigned host port. No top-level `services` context, no auto-injected env var — set `REDIS_PORT` yourself.

## Health checks

Actions waits for a service only if the image has a health check. No `healthcheck:` block (that's docker-compose) — pass raw `docker create` flags via `options:`:

```yaml
services:
  postgres:
    image: postgres:16
    env:
      POSTGRES_PASSWORD: ci
    options: >-
      --health-cmd "pg_isready"
      --health-interval 10s
      --health-timeout 5s
      --health-retries 5
```

(`>-` = folded scalar: newlines become spaces, so the flags reach Docker as one string.)

## Odds and ends

- Private registry: credentials under `services.<label>.credentials` (`username`/`password`).
- Service logs: job log, "Initialize containers" section.
