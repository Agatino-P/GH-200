# Self-hosted runners — setup, end to end

Mental model: **GitHub gives you a script, you run it on your machine, the machine registers itself and waits for jobs.** You start in the **Settings UI**, not in a workflow.

## Steps

**1. Pick the scope and open "New self-hosted runner"** — GitHub → **Settings → Actions → Runners → New self-hosted runner**, at one of three levels:
- **Repository** — serves that one repo
- **Organization** — shared across repos (managed via runner groups)
- **Enterprise** — shared across orgs

**2. Choose OS + architecture** (Linux/Windows/macOS, x64/ARM). GitHub then shows a copy-paste block of shell commands to run **on the machine you want to become a runner**.

**3. On that machine, run the three phases:**
```bash
# a) Download the runner application (the open-source actions/runner)
mkdir actions-runner && cd actions-runner
curl -o actions-runner.tar.gz -L https://github.com/actions/runner/releases/...
tar xzf actions-runner.tar.gz

# b) Configure — registers the machine with GitHub
./config.sh --url https://github.com/<owner>/<repo> --token <REGISTRATION_TOKEN>
#   also sets: runner name, labels, runner group, work folder

# c) Run — start listening for jobs
./run.sh
```
The **registration token** is the short-lived token shown on the Settings page (also available via REST API). `config.sh` is the moment the runner joins GitHub.

**4. Run it as a service** (survives reboots) instead of `./run.sh`:
```bash
sudo ./svc.sh install
sudo ./svc.sh start
```

**5. Target it from a workflow** with `runs-on`:
```yaml
runs-on: self-hosted                 # any self-hosted runner
runs-on: [self-hosted, linux, gpu]   # narrow by custom labels
```

## Gotchas

- **You provision the machine.** The tool cache starts **empty** — install Node/Python/Docker yourself or use `setup-*` actions. GitHub supplies only the runner agent.
- **Requirements:** outbound HTTPS to GitHub (no inbound needed); supported OS. The runner **auto-updates** by default.
- **Labels** route jobs; **runner groups** (org/enterprise) control which repos may use which runners.
- **Security:** never attach a self-hosted runner to a **public** repo — a fork PR could run arbitrary code on your hardware. Self-hosted is for private/trusted use.

One line: **Settings → New runner → copy the script → on your box run `config.sh` (register) then `run.sh` (listen) → reference with `runs-on: self-hosted`.**
