# GH-200 — Topic 4A Recap: Runner Networking & Access Boundaries

**Domain 4 (Enterprise, highest weight 20–25%) · Objective 4.4 — IP allow lists & runner networking.**
Verified live against official GitHub docs (Enterprise Cloud) on 2026-06-22. This area is current-state and still evolving; re-verify specifics near exam time.

Cheat file companion: `GH-200_Cheat_4A_-_Runner_Networking_and_Access_Boundaries.md`.

---

## The master distinction (carry this into every 4A question)

Two problems look alike but are solved by different tools. Crossing them is the trap that caught both quiz misses.

- **Egress identity** — *"What source IP does my runner present?"* What an **IP allow list** (and any target firewall) cares about. Fix = make the runner's IP **predictable**: self-hosted runners, or **static-IP larger runners**.
- **Private reachability** — *"How does my runner reach a resource with no public endpoint?"* (DB, Artifactory, on-prem API). Fix = put the runner **onto/into** your network: **Azure VNET**, **WireGuard overlay**, or **API gateway + OIDC**.

A static IP does **not** grant private reachability; a VNET does **not** (by default) give you an allow-listable egress IP.

---

## Bit 1 — IP allow lists

### What it is and where it lives
- Restricts access to your **private** resources to approved source IPs. **Public resources stay reachable.**
- **GitHub Enterprise Cloud only.** A plain Free/Team org can't use it.
- Configured **org-level** (Settings → Security → **Authentication security → IP allow list**) or **enterprise-level** (inherited by all member orgs).
  - Org owners can add their own entries but **cannot edit** inherited enterprise entries; enterprise owners **cannot manage** org-added entries.
- Entries use **CIDR notation** (single IP or range).

### Role-blind → lockout risk
Applies to **everyone**, including enterprise/org owners, repo admins, and outside collaborators. Best practice: keep **more than one owner** so a bad entry doesn't lock everyone out. (Caching means add/remove can take a few minutes to take effect.)

### Trap — adding entries ≠ enforcing (two distinct actions)

```
1. Add IP/CIDR entries to the list.
2. Tick "Enable IP allow list"   ← only THIS starts enforcing.
```

A full list with the toggle **off** restricts nothing.

### The two toggles that actually exist (corrected the plan's wording)
The §7d plan mistakenly called one "the enable-for-Actions toggle." **There is no Actions toggle.** The two real controls under "IP allow list":

1. **Enable IP allow list** — the enforcement switch.
2. **Enable IP allow list configuration for installed GitHub Apps** — auto-imports IP ranges that installed GitHub Apps *declare* for themselves. Notably, these App IPs are added **irrespective of whether the allow list is currently enabled**.

Actions traffic is gated **solely by the runner's IP** — there is no "let Actions through" button. That's the whole reason the hosted-runner conflict exists.

### The hosted-runner conflict (headline of Bit 1)
Standard GitHub-hosted runners (`ubuntu-latest`, etc.) run on **Azure** and share the **Azure datacenter IP ranges** — which are **huge, shared across all GitHub customers, and rotate (the published list updates weekly)**. Allow-listing them is impractical *and* weakens the control (you'd trust every other tenant's runners).

- Older (GHES) framing, stated absolutely: with an IP allow list you **cannot** use GitHub-hosted runners; must use self-hosted (a standard runner's `actions/checkout` returns **403**).
- Current **GHEC** resolution: you *can* combine an allow list with Actions, but only with runners whose IPs you control —
  - **self-hosted runners** (add their egress IPs), or
  - **GitHub-hosted *larger* runners with the static-IP feature** (add the fixed range).
  - Then **add the runner's IP/range to the allow list**.

### Non-obvious carve-outs (likely distractors)
- **Dependabot** is a first-party GitHub App — its repository access is **exempt** from the allow list.
- **GitHub Apps using server-to-server installation tokens** are **not currently restricted** by the allow list.
- Configuring an **org** IP allow list makes **GitHub Codespaces unusable** for that org's repos.
- A **Pages** site built by a *custom* Actions workflow needs an allow-list rule for its build runner (default-workflow builds don't).

---

## Bit 2 — Static-IP larger runners & private networking

### Path 1 — Static IP larger runners (the allow-list workaround)
Solves **egress identity**. Enterprise Cloud, opt-in: a **fixed IP range** is assigned to larger-runner instances, which you add to your allow list — explicitly usable **in conjunction with** the IP allow list to run hosted Actions and IP allow-listing at the same time. Modern instances get **two ranges** in different geographies (also lets concurrency scale **beyond the old 500 limit**).

Why not just allow-list standard runners? The runner reference says it directly: too many ever-changing ranges; **use larger runners with a static IP range, or self-hosted runners** instead.

### Path 2 — Azure VNET private networking (main private-reachability path)
Solves **private reachability** via **VNET injection**:

> The runner's **NIC is deployed into your Azure subnet**, while the **runner VM stays in GitHub-owned infrastructure**.

Because the NIC sits in your subnet, your VNET policies apply to the runner: **NSG outbound rules**, plus access to on-prem / other-cloud via **ExpressRoute or VPN**.

- **Benefits:** private connectivity without opening internet ports; full outbound-policy control; network-log monitoring of all runner traffic.
- **Supported runners:** **2–64 vCPU Ubuntu and Windows** larger runners.
- **Setup order:** configure **Azure resources first** (subnet + NSG via the provided `.bicep`), then create a **network configuration** in GitHub and associate it to a **runner group**; all runners in that group then use the VNET.
- **Subnet sizing:** make available IPs exceed **max job concurrency** (docs suggest ~30% buffer; one GitHub Learn page says 20% — learn the *principle*, not the exact %).

### Paths 3 & 4 — non-Azure options (lighter weight)
For private reachability without Azure, both are **patterns you build** and work with **standard runners** too (they don't depend on GitHub networking config):
- **API gateway + OIDC** — workflow authenticates to a service outside Actions using an OIDC token.
- **WireGuard overlay** — run WireGuard on both the runner and a host in your private network to form an overlay (no separate gateway infra).

### Headline trap — Static IP ⊕ Azure VNET are mutually exclusive
- VNET runners use **dynamic IPs** (the default); you **cannot** also assign the static-IP feature to them.
- Worse for allow-listing: with VNET on **Azure default outbound access**, egress IPs are **unpredictable** and **cannot** be added to the IP allow list. You'd need a **stable outbound IP (NAT gateway)** to make VNET egress allow-listable.
- **macOS larger runners** support **neither** Azure VNET **nor** static IPs.

---

## Quiz outcomes (exam-style)

- **Bit 1 — 4/5.** Miss: the toggle-name item — selected *"...for GitHub Actions runners"*; correct is *"Enable IP allow list configuration for installed GitHub Apps."* There is **no Actions toggle**. Resolved.
- **Bit 2 — 4/5.** Miss: marked **static IP** as a workable fix for giving a **standard** runner **private reachability**; wrong on two counts — static IP is a larger-runner/GHEC feature (scope), and it solves egress identity, **not** reachability (wrong problem). Resolved.

**Pattern:** both misses sat at the **conceptual boundary**, not the facts — *egress identity vs private reachability*, and *what each tool is for*. That distinction is the lead keeper.

---

## Honesty / freshness flags
1. **GHES vs GHEC tension:** the "hosted runners are wholly incompatible with an allow list" line comes from an **Enterprise Server** page; current **Enterprise Cloud** docs supersede it with the *larger-runners + static IP* exception. Treat GHEC as authoritative for GH-200, but the exam may lean on the older absolute framing.
2. **"Artifacts are exempt from the allow list"** — seen only as a **community claim**, **not** confirmed in official docs. Don't treat as exam-grade.
3. **Evolving:** runner NICs are moving to a GitHub **service subscription** (assigned IPs from your subnet); **VNET failover** (secondary, possibly cross-region subnet, manual switch) is **public preview**. Could change.
4. **Org vs enterprise level for VNET config:** concept page says org owners on **Team** can configure at org level; enterprise doc says initial Azure setup must be at **enterprise** level with orgs enabled by policy. Different scopes — don't over-specify the level unless the scenario names the plan.
