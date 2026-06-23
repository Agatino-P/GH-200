# GH-200 Cheat — 4A: Runner Networking & Access Boundaries

*Last-week review. Full notes: `GH-200_Topic_4A_-_Runner_Networking_and_Access_Boundaries.md`. (Domain 4 · 4.4)*

---

### ★ MASTER DISTINCTION — egress identity vs private reachability
- **Egress identity** = predictable *source IP* the runner presents → for **IP allow lists** / target firewalls. Tools: **self-hosted** or **static-IP larger runners**.
- **Private reachability** = getting onto/into a network with **no public endpoint** → DB, Artifactory, on-prem API. Tools: **Azure VNET**, **WireGuard**, **API gateway + OIDC**.
- **Don't cross them:** a static IP does NOT grant reachability; a VNET does NOT (by default) give an allow-listable egress IP.

### ★ NO "Actions" toggle on an IP allow list
Only two controls exist:
1. **Enable IP allow list** (enforcement on/off)
2. **Enable IP allow list configuration for installed GitHub Apps** (auto-imports App-declared IPs; happens even if the list isn't enabled)

Actions is gated **purely by the runner's IP**. Distractor bait: *"...for Actions runners"*, *"...for Actions and Pages."*

### ★ Static IP ⊕ Azure VNET = mutually exclusive
- VNET runners use **dynamic IPs**; can't also assign static IP.
- VNET + **Azure default outbound** ⇒ egress IPs **unpredictable**, **not** allow-listable → need **NAT gateway / stable outbound IP**.

---

### IP allow list — fast facts
- **GHEC only.** Gates **PRIVATE** resources (public stays open).
- **Role-blind** — applies to owners, repo admins, outside collaborators too → **lockout risk**, keep ≥2 owners.
- **Adding entries ≠ enforcing** — must tick *Enable IP allow list*.
- Org-level **or** enterprise-level (enterprise entries inherited; org can add but not edit inherited).
- CIDR notation.

### Hosted-runner conflict
- Standard hosted runners = **wide + shared + weekly-rotating Azure IPs** ⇒ can't practically allow-list (and it weakens control).
- Under an allow list, use **self-hosted** OR **static-IP larger runners**; add the runner IP/range to the list. (Standard runner ⇒ `checkout` 403.)

### Carve-outs / exemptions (distractors)
- **Dependabot** = exempt (first-party App).
- **GitHub App server-to-server installation tokens** = not currently restricted.
- **Codespaces** = unusable for org repos when an org allow list is set.

### Private networking paths
- **Static IP larger runner** → egress identity; fixed range; usable *with* allow list; dual ranges, scales past 500 concurrency.
- **Azure VNET** → reachability; **VNET injection** = NIC in your subnet, **VM stays GitHub-side**; inherits NSG / ExpressRoute / VPN; **2–64 vCPU Ubuntu + Windows only**; setup = Azure resources first → network config → runner group; size subnet > max concurrency.
- **API gateway + OIDC** and **WireGuard overlay** → reachability, **work with standard runners** (patterns you build).

### OS/size exclusions
- **macOS larger runners** = **no** Azure VNET, **no** static IP.

---

### Watch-outs (uncertain / evolving — don't over-commit)
- "Artifacts exempt from allow list" = **community claim, unverified**.
- GHES docs say hosted runners wholly incompatible (older/absolute); GHEC adds the static-IP exception.
- VNET NICs moving to a GitHub service subscription; **VNET failover** in public preview.
- Subnet buffer %: docs ~30% vs GitHub Learn 20% — know the *principle* (size > max concurrency), not the number.
