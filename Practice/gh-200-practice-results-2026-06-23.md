# Practice Assessment Results: June 23, 2026

**Practice Assessment for GH-200: GitHub Actions** · Completion time: 13 minutes

## Overall Results

Score: **90%** · Target: 77%+ across multiple attempts

Performance by section: Section 1 — 94% · Section 2 — 100% · Section 3 — 86% · Section 4 — 50%

Banner shown: "Congratulations, you passed all the sections!" (reported as-is; it sits oddly against the 50% Section 4 figure).

> Note: The full multiple-choice options (the distractors) are **not** present in the source HTML. The "Answer Summary" view only renders the selected option, the correct option, and a rationale per question. To capture the other choices, re-open the assessment itself (not the results page).

---

## Answer Summary (30 questions)

**Q1.** Why use the following YAML: `if: contains(github.event.issue.labels.*.name, 'bug')`?
- Your answer: To ensure the script only runs when the issue is labeled as a bug. ✓
- Correct: same.
- Rationale: This YAML condition ensures the script runs only when the issue is labeled as a bug.

**Q2.** Which of these can NOT trigger a GitHub Actions workflow?
- Your answer: Opening a new tab in your browser. ✓
- Correct: same.
- Rationale: Opening a new tab in your browser cannot trigger a workflow.

**Q3.** What can trigger a workflow for deploying to Microsoft Azure?
- Your answer: Any event. ✓
- Correct: same.
- Rationale: Any event can trigger a workflow for deploying to Microsoft Azure.

**Q4.** How do you trigger a workflow on a push event?
- Your answer: Use `on: push` in the workflow. ✓
- Correct: same.
- Rationale: The `run: push` keyword is not used to trigger workflows. *(Note: the rationale text here describes a wrong option rather than the correct one — that's how it reads in the source.)*

**Q5.** Which command sets the debug message to 'This is an error message'?
- Your answer: `echo "::error::This is an error message"` ✓
- Correct: same.
- Rationale: This is the correct syntax for setting an error message in GitHub Actions.

**Q6.** What is a step in GitHub Actions?
- Your answer: An individual task within a job. ✓
- Correct: same.
- Rationale: A step is an individual task within a job in GitHub Actions.

**Q7.** What is the `jobs` section used for in a workflow?
- Your answer: Defines tasks executed by the workflow. ✓
- Correct: same.
- Rationale: The `jobs` section defines tasks executed by the workflow.

**Q8.** How do you grant your GitHub repository access to Azure?
- Your answer: Authenticate to Azure with GitHub. ✗ **Incorrect**
- Correct: Manage credentials using GitHub Secrets.
- Rationale: GitHub Secrets can securely manage credentials for Azure.

**Q9.** How do you ensure your Azure credentials aren't stored in plain text?
- Your answer: Use GitHub Secrets. ✓
- Correct: same.
- Rationale: GitHub Secrets securely store sensitive information like Azure credentials.

**Q10.** What is Dependabot?
- Your answer: A tool for keeping dependencies up to date. ✓
- Correct: same.
- Rationale: Dependabot is a tool for keeping dependencies up to date.

**Q11.** Which of the following does GitHub Secret NOT secure?
- Your answer: Sensitive information inside workflow logs. ✓
- Correct: same.
- Rationale: GitHub Secrets do not secure sensitive information inside workflow logs.

**Q12.** How does `env` work in GitHub Actions?
- Your answer: Sets environment variables for use in jobs and steps. ✓
- Correct: same.
- Rationale: The `env` keyword sets environment variables for use in jobs and steps.

**Q13.** What are GitHub Actions used for?
- Your answer: All of these functions. ✓
- Correct: same.
- Rationale: GitHub Actions can perform all of these functions.

**Q14.** What can GitHub Actions NOT be used for?
- Your answer: Upload a new secret to GitHub Secrets. ✓
- Correct: same.
- Rationale: GitHub Actions cannot upload new secrets to GitHub Secrets.

**Q15.** How do you reference a reusable workflow in GitHub Actions?
- Your answer: Use `uses` keyword. ✓
- Correct: same.
- Rationale: The `uses` keyword is used to reference a reusable workflow in GitHub Actions.

**Q16.** How do you create a GitHub Actions workflow?
- Your answer: Define it in a YAML file in `.github/workflows/`. ✓
- Correct: same.
- Rationale: Workflows are defined in YAML files located in the `.github/workflows/` directory.

**Q17.** What does GitHub Actions' matrix allow?
- Your answer: Run workflows in parallel across different configurations. ✓
- Correct: same.
- Rationale: The matrix allows running workflows in parallel across different configurations.

**Q18.** What is the purpose of GitHub Actions' caching mechanism?
- Your answer: Reduce workflow execution time. ✓
- Correct: same.
- Rationale: The caching mechanism reduces workflow execution time.

**Q19.** Artifacts from a GitHub Actions workflow can be saved with what action?
- Your answer: `actions/upload-artifact` ✓
- Correct: same.
- Rationale: The `actions/upload-artifact` action is used to save artifacts from a workflow.

**Q20.** Which action accesses a repository's code in a GitHub Actions virtual machine?
- Your answer: `actions/checkout` ✓
- Correct: same.
- Rationale: `actions/checkout` is used to access a repository's code in a virtual machine.

**Q21.** What is GitHub Packages used for?
- Your answer: Hosting and managing packages. ✓
- Correct: same.
- Rationale: GitHub Packages is used for hosting and managing packages.

**Q22.** What is GitHub Script?
- Your answer: A programming language that compiles to JavaScript. ✗ **Incorrect**
- Correct: A workflow action that enables GitHub API access from GitHub Actions.
- Rationale: GitHub Script is a workflow action that allows access to the GitHub API from GitHub Actions.

**Q23.** What is the difference between GitHub Script and GitHub Actions?
- Your answer: GitHub Actions is a workflow engine that automates actions. GitHub Script is one of the actions available for use in a workflow. ✓
- Correct: same.
- Rationale: GitHub Actions is a workflow engine, and GitHub Script is one of the actions available for use in workflows.

**Q24.** You need to create a custom GitHub Action in Ruby. Which action type would you choose?
- Your answer: Docker container action. ✓
- Correct: same.
- Rationale: Docker container actions are suitable for custom actions in Ruby.

**Q25.** What are the three types of GitHub Actions?
- Your answer: Container actions, JavaScript actions, composite actions. ✓
- Correct: same.
- Rationale: These are the three types of GitHub Actions.

**Q26.** Which keywords are required for a valid `action.yml` file?
- Your answer: `name`, `runs`, `description`. ✓
- Correct: same.
- Rationale: `name`, `runs`, and `description` are required keywords for a valid `action.yml` file.

**Q27.** Which file is essential to set up a GitHub Action?
- Your answer: `action.yml`. ✓
- Correct: same.
- Rationale: `action.yml` is the essential file for setting up a GitHub Action.

**Q28.** Which of the following is NOT a GitHub Actions feature?
- Your answer: Repository metrics. ✓
- Correct: same.
- Rationale: Repository metrics are not a feature of GitHub Actions.

**Q29.** How is a self-hosted runner different from a GitHub-hosted runner?
- Your answer: Self-hosted runners are managed by you, not GitHub. ✓
- Correct: same.
- Rationale: Self-hosted runners are managed by you, not GitHub.

**Q30.** What is GitHub Advanced Security (GHAS)?
- Your answer: A tool for analyzing source code for vulnerabilities. ✗ **Incorrect**
- Correct: An application security solution that empowers developers.
- Rationale: GHAS is more comprehensive than just analyzing source code for vulnerabilities.

---

**Result: 27/30.** Missed: Q8, Q22, Q30.
