# GH-200 Practice Assessment — Full Questions & Options
**Practice Assessment for GH-200: GitHub Actions** · June 23, 2026 · Score 90% (27/30)

Options extracted from the per-question screenshots. Legend: ✅ correct answer · ❌ your incorrect selection · ⬜ other option.

---

**Q1. Why use the following YAML in GitHub Script: `if: contains(github.event.issue.labels.*.name, 'bug')`?**
- ✅ To ensure the script only runs when the issue is labeled as a bug.
- ⬜ To enforce issue creation policy.
- ⬜ To automatically flag bug-related commits.
- ⬜ To prevent the script from executing on pull requests.

Rationale: This YAML condition ensures the script runs only when the issue is labeled as a bug.

---

**Q2. Which of these can NOT trigger a GitHub Action workflow?**
- ⬜ Making a commit
- ✅ Opening a new tab in your browser
- ⬜ Merging a branch
- ⬜ Opening an issue

Rationale: Opening a new tab in your browser cannot trigger a workflow.

---

**Q3. What can trigger a workflow for deploying to Microsoft Azure?**
- ⬜ Only commit events
- ⬜ Events that affect the repository's default branch
- ✅ Any event
- ⬜ Only pull request events

Rationale: Any event can trigger a workflow for deploying to Microsoft Azure.

---

**Q4. How do you trigger a workflow on a push event?**
- ✅ Use `on: push` in the workflow
- ⬜ Use `run: push`
- ⬜ Set it in the repository settings
- ⬜ Manually run the workflow

Rationale: The `run: push` keyword is not used to trigger workflows.

---

**Q5. Which command sets the debug message to 'This is an error message'?**
- ✅ `echo "::error::This is an error message"`
- ⬜ `echo "error=This is an error message"`
- ⬜ `echo "::error::message=This is an error message"`
- ⬜ `echo "::error::This is an error message::"`

Rationale: This is the correct syntax for setting an error message in GitHub Actions.

---

**Q6. What is a step in GitHub Actions?**
- ✅ An individual task within a job
- ⬜ A repository event
- ⬜ An entire workflow
- ⬜ A CI/CD pipeline

Rationale: A step is an individual task within a job in GitHub Actions.

---

**Q7. What is the jobs section used for in a workflow?**
- ✅ Defines tasks executed by the workflow
- ⬜ Specifies workflow triggers
- ⬜ Sets up repository secrets
- ⬜ Automates package installations

Rationale: The jobs section defines tasks executed by the workflow.

---

**Q8. How do you grant your GitHub repository access to Azure?**
- ⬜ It happens automatically
- ❌ Authenticate to Azure with GitHub *(your selection — incorrect)*
- ✅ Manage credentials using GitHub Secrets
- ⬜ Manage credentials by generating tokens locally

Rationale: GitHub Secrets can securely manage credentials for Azure.

---

**Q9. How do you ensure your Azure credentials aren't stored in plain text?**
- ✅ Use GitHub Secrets
- ⬜ Use GitHub token to authenticate into Azure
- ⬜ Put credentials directly in the workflow file
- ⬜ Encrypt your credentials in a separate file.

Rationale: GitHub Secrets securely store sensitive information like Azure credentials.

---

**Q10. What is Dependabot?**
- ✅ A tool for keeping dependencies up to date
- ⬜ A tool for detecting and fixing code vulnerabilities
- ⬜ A service for managing CI/CD pipelines
- ⬜ A GitHub Marketplace service

Rationale: Dependabot is a tool for keeping dependencies up to date.

---

**Q11. Which of the following does GitHub Secret NOT secure?**
- ✅ Sensitive information inside workflow logs.
- ⬜ API keys.
- ⬜ Database credentials.
- ⬜ Azure credentials.

Rationale: GitHub Secrets do not secure sensitive information inside workflow logs.

---

**Q12. How does env work in GitHub Actions?**
- ✅ Sets environment variables for use in jobs and steps
- ⬜ Sets the file path for job logs
- ⬜ Automates Docker container setup
- ⬜ Specifies trigger conditions

Rationale: The `env` keyword sets environment variables for use in jobs and steps.

---

**Q13. What are GitHub Actions used for?**
- ⬜ To automate software development tasks
- ⬜ To facilitate CI/CD
- ⬜ To integrate infrastructure as code
- ✅ All of these functions

Rationale: GitHub Actions can perform all of these functions.

---

**Q14. What can GitHub Actions NOT be used for?**
- ⬜ Automatically run test suites on each push
- ⬜ Kick off a review process
- ⬜ Automate common repetitive tasks
- ✅ Upload a new secret to GitHub Secrets

Rationale: GitHub Actions cannot upload new secrets to GitHub Secrets.

---

**Q15. How do you reference a reusable workflow in GitHub Actions?**
- ✅ Use `uses` keyword.
- ⬜ Use `runs` keyword.
- ⬜ Use `jobs` keyword.
- ⬜ Use `trigger` keyword.

Rationale: The `uses` keyword is used to reference a reusable workflow in GitHub Actions.

---

**Q16. How do you create a GitHub Actions workflow?**
- ✅ Define it in a YAML file in `.github/workflows/`
- ⬜ Set it up in the repository's settings
- ⬜ Use the GitHub UI to generate it
- ⬜ Upload a custom shell script

Rationale: Workflows are defined in YAML files located in the `.github/workflows/` directory.

---

**Q17. What does GitHub Actions' matrix allow?**
- ⬜ Run workflows on the same OS
- ✅ Run workflows in parallel across different configurations
- ⬜ Handle multiple GitHub repositories
- ⬜ Automate issue tracking

Rationale: The matrix allows running workflows in parallel across different configurations.

---

**Q18. What is the purpose of GitHub Actions' caching mechanism?**
- ⬜ Save workflow logs.
- ✅ Reduce workflow execution time.
- ⬜ Store repository secrets.
- ⬜ Manage artifacts.

Rationale: The caching mechanism reduces workflow execution time.

---

**Q19. Artifacts from a GitHub Actions workflow can be saved with what action?**
- ✅ `actions/upload-artifact`
- ⬜ `actions/checkout@v3`
- ⬜ `actions/download-artifact`
- ⬜ `actions/cache`

Rationale: The `actions/upload-artifact` action is used to save artifacts from a workflow.

---

**Q20. Which action accesses a repository's code in a GitHub Actions virtual machine?**
- ⬜ `actions/upload-artifact`
- ✅ `actions/checkout`
- ⬜ `npm install`
- ⬜ `actions/setup-node`

Rationale: `actions/checkout` is used to access a repository's code in a virtual machine.

---

**Q21. What is GitHub Packages used for?**
- ✅ Hosting and managing packages
- ⬜ Automating builds
- ⬜ Automating issue tracking
- ⬜ Handling pull requests

Rationale: GitHub Packages is used for hosting and managing packages.

---

**Q22. What is GitHub Script?**
- ❌ A programming language that compiles to JavaScript. *(your selection — incorrect)*
- ⬜ An automation syntax for GitHub Shell.
- ✅ A workflow action that enables GitHub API access from GitHub Actions.
- ⬜ A way to automate workflows on a local machine.

Rationale: GitHub Script is a workflow action that allows access to the GitHub API from GitHub Actions.

---

**Q23. What is the difference between GitHub Script and GitHub Actions?**
- ⬜ GitHub Actions is for automating build and release pipelines. It was written in the GitHub Script programming language.
- ✅ GitHub Actions is a workflow engine that automates actions. GitHub Script is one of the actions available for use in a workflow.
- ⬜ GitHub Actions automates workflows outside of GitHub. GitHub Script automates workflows inside GitHub.
- ⬜ GitHub Actions is primarily used for CI/CD purposes, while GitHub Script is not.

Rationale: GitHub Actions is a workflow engine, and GitHub Script is one of the actions available for use in workflows.

---

**Q24. You need to create a custom GitHub Action in Ruby. Which action type would you choose?**
- ⬜ JavaScript action
- ⬜ Run step
- ✅ Docker container action
- ⬜ Bash script

Rationale: Docker container actions are suitable for custom actions in Ruby.

---

**Q25. What are the three types of GitHub Actions?**
- ✅ Container actions, JavaScript actions, composite actions
- ⬜ Embedded actions, composite actions, container actions
- ⬜ Workflows, triggers, composite actions
- ⬜ Sequential actions, parallel actions, and composite actions

Rationale: These are the three types of GitHub Actions.

---

**Q26. Which keywords are required for a valid action.yml file?**
- ⬜ `name, runs, composite`
- ✅ `name, runs, description`
- ⬜ `name, description, branding`
- ⬜ `name, description, composite`

Rationale: name, runs, and description are required keywords for a valid action.yml file.

---

**Q27. Which file is essential to set up a GitHub Action?**
- ⬜ `Config.yml`
- ✅ `action.yml`
- ⬜ `Settings.yml`
- ⬜ `Package.json`

Rationale: action.yml is the essential file for setting up a GitHub Action.

---

**Q28. Which of the following is NOT a GitHub Actions feature?**
- ⬜ Reusable workflows
- ⬜ Docker container support
- ✅ Repository metrics
- ⬜ Custom event triggers

Rationale: Repository metrics are not a feature of GitHub Actions.

---

**Q29. How is a self-hosted runner different from a GitHub-hosted runner?**
- ✅ Self-hosted runners are managed by you, not GitHub.
- ⬜ Self-hosted runners run only GitHub-provided workflows.
- ⬜ Self-hosted runners are free for unlimited workflows.
- ⬜ Self-hosted runners only run locally.

Rationale: Self-hosted runners are managed by you, not GitHub.

---

**Q30. What is GitHub Advanced Security (GHAS)?**
- ⬜ An automated tool for managing project dependencies
- ✅ An application security solution that empowers developers
- ❌ A tool for analyzing source code for vulnerabilities *(your selection — incorrect)*
- ⬜ A platform for tracking dependencies

Rationale: GHAS is more comprehensive than just analyzing source code for vulnerabilities.

---

## Summary
**27/30 correct.** Missed: Q8 (Azure repo access → GitHub Secrets), Q22 (GitHub Script definition), Q30 (GHAS scope).

> Note on ordering: the screenshots in the source document are not in results-page order. Questions above are numbered as they appear in the screenshots (Question N of 30 labels).
