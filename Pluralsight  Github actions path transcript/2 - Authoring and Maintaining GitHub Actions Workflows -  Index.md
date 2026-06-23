### **Course: Authoring and Maintaining GitHub Actions Workflows**

* **Chapter:** Course Overview 
    * **Lesson:** Course Overview 
* **Chapter:** Triggering Workflows with Events 
    * **Lesson:** Creating and Running a Workflow 
    * **Lesson:** Push Triggers Workflow Run #2 
    * **Lesson:** Triggering on a Schedule 
    * **Lesson:** Manual Triggers with workflow_dispatch 
    * **Lesson:** dotnet build on Every Push 
    * **Lesson:** Detecting a Build Failure 
    * **Lesson:** Using the gh CLI to View Runs and Workflows 
* **Chapter:** Using Steps on Runners 
    * **Lesson:** Jobs Have Steps 
    * **Lesson:** A New Workflow for the Upper Build 
    * **Lesson:** What Software Is Pre-installed on ubuntu-latest? 
    * **Lesson:** Adding actions/setup-go 
    * **Lesson:** Understanding actions/checkout 
    * **Lesson:** An Invalid Workflow File Causes an Immediate Failure 
    * **Lesson:** Set Working Directory on the Multiline Run Step 
    * **Lesson:** go-version-file and Cached vs. Downloaded Go Version 
    * **Lesson:** Fix Caching of Dependencies 
    * **Lesson:** Running on macos-latest 
    * **Lesson:** Targeting a Job to Use a Self-hosted Runner 
* **Chapter:** Injecting Secrets and Environment Variables 
    * **Lesson:** The gh CLI Provides a Wealth of Information 
    * **Lesson:** Authenticating with GH_TOKEN 
    * **Lesson:** Injecting the GH_TOKEN Environment Variable 
    * **Lesson:** Commenting on Issues with actions/github-scripts 
    * **Lesson:** Set Token Permissions to Write to Issues 
    * **Lesson:** Testing the Issue Opened Trigger 
    * **Lesson:** Adding a Secret for an OPENAI_API_KEY 
    * **Lesson:** Testing Code Butler's Chat Mode 
    * **Lesson:** Conditional Jobs with If 
    * **Lesson:** Another Conditional Job for Code Butler's Review Mode 
    * **Lesson:** Log the Event Payload and Disable the Workflow 
* **Chapter:** Publishing Artifacts 
    * **Lesson:** Monitor Workflow Runs Inside VSCode 
    * **Lesson:** actions/upload-artifact 
    * **Lesson:** Matrix Strategy for Runner OS 
    * **Lesson:** Download and Delete Artifacts 
    * **Lesson:** Using a Script to Cross Compile 
    * **Lesson:** Grouping Logs with Workflow Commands 
    * **Lesson:** Creating a GitHub Release 
    * **Lesson:** Updating an Existing Release 
    * **Lesson:** Release on Tags Only 
    * **Lesson:** Workflow Status Badges 
    * **Lesson:** Workflow to Build an Image 
    * **Lesson:** Push the Image to ghcr.io to Create a Package 
* **Chapter:** Deployment Pipelines 
    * **Lesson:** Building an Image for the dotnet Web API 
    * **Lesson:** Workflow to Push an Image to Docker Hub 
    * **Lesson:** Production Environment Requires Approval to Deploy 
    * **Lesson:** Test Azure Login with Approval 
    * **Lesson:** azure/webapps-deploy Action 
    * **Lesson:** Record the WebApp URL on the Deployment 
    * **Lesson:** The Entire CD Pipeline Works! 
    * **Lesson:** Triggering a New Workflow on Deployment Created 
    * **Lesson:** Passing Environment Variables with GITHUB_ENV Environment File 
    * **Lesson:** Passing Outputs between Dependent Jobs 
    * **Lesson:** Using a Job Container to Provide the MySQL CLI 
    * **Lesson:** Connecting to a MySQL Service Container! 
    * **Lesson:** Setting up a CodeQL Workflow 
    * **Lesson:** Alerts from the security-and-quality Suite 
