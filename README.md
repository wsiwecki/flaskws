# Overview

<TODO: complete this with an overview of your project>

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project

https://trello.com/invite/b/HPVtYyJR/ATTI53b8619f331e536c95f4123178f9ba4d301ED1B4/azure-devops-ci-cd

* A link to a spreadsheet that includes the original and final project plan>:  https://docs.google.com/spreadsheets/d/1LD9J6WBjs48r34Q5RipeMulNv3CYptiQk0NJBGMFYB0/edit?usp=sharing

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>
* ![00_diagram](https://user-images.githubusercontent.com/58573764/234246730-23d60c6e-aa59-4206-94b4-e4702173fd3c.jpg)


<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
wojciech_siwecki [ ~/flaskws ]$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[2.431574790057212]}
```

* Output of streamed log files from deployed application

[{"log_time":"2023-04-20T13:42:18.4948413Z","id":"5b0487d0-b300-4e7f-905b-98c891ef633c","message":"Updating submodules.","type":0,"details_url":null},{"log_time":"2023-04-20T13:42:19.9101254Z","id":"ef539660-b2e3-491b-8ad1-7d5cfe03f092","message":"Preparing deployment for commit id '234c71d4-0'.","type":0,"details_url":null},{"log_time":"2023-04-20T13:42:20.6949162Z","id":"58db5ec4-e04d-4956-9ba8-52b0926db57a","message":"PreDeployment: context.CleanOutputPath False","type":0,"details_url":null},{"log_time":"2023-04-20T13:42:20.9349184Z","id":"4c32d38c-26c8-4322-8bdc-bf8a89803064","message":"PreDeployment: context.OutputPath /home/site/wwwroot","type":0,"details_url":null},{"log_time":"2023-04-20T13:42:21.4297513Z","id":"5054276f-75fd-4a35-9ea3-7b3800aace02","message":"Repository path is /tmp/zipdeploy/extracted","type":0,"details_url":null},{"log_time":"2023-04-20T13:42:21.6802218Z","id":"0275a7aa-b3b6-4cce-aff8-94bf86c7619a","message":"Running oryx build...","type":0,"details_url":"https://flaskws.scm.azurewebsites.net/api/deployments/234c71d4-0a1a-48d9-a9a0-d6296d431a16/log/0275a7aa-b3b6-4cce-aff8-94bf86c7619a"},{"log_time":"2023-04-20T13:45:37.5071637Z","id":"fa2a5a35-c75a-4002-b766-023df65de838","message":"Running post deployment command(s)...","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:37.6902675Z","id":"310418b1-e981-497e-98c7-2522e7a19b38","message":"","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:37.8706481Z","id":"1a86b455-4998-45ba-ab36-fb371c983265","message":"Generating summary of Oryx build","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:38.0688952Z","id":"f4893742-6b31-44e6-a2b1-e1876bf0f2eb","message":"Parsing the build logs","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:38.1970974Z","id":"0a95a23e-a6c7-41c0-9bc6-1900b2588903","message":"Found 0 issue(s)","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:38.2986218Z","id":"37556505-9672-4c4d-b46e-5a1abcdb10e6","message":"","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:38.4631251Z","id":"1322db72-4374-404a-9d55-0229d890161f","message":"Build Summary :","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:38.6476767Z","id":"14a9980f-ed44-4cdd-9078-27b27b469ccb","message":"===============","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:38.8316054Z","id":"5ae777ec-4ac4-47e3-860e-08abef7bc294","message":"Errors (0)","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:39.0299581Z","id":"c85b3ae1-e4b1-4076-a625-7022c4092c5d","message":"Warnings (0)","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:39.2135824Z","id":"70e09383-6306-43cc-a69b-b5780fd42a2b","message":"","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:39.5397932Z","id":"053cf017-a4b5-4a56-8c7f-e5cd2062af3a","message":"Triggering recycle (preview mode disabled).","type":0,"details_url":null},{"log_time":"2023-04-20T13:45:39.7573572Z","id":"6b853372-f35d-4743-ace7-41aa9c99996d","message":"Deployment successful. deployer = GITHUB_ZIP_DEPLOY deploymentPath = ZipDeploy. Extract zip. Remote build.","type":0,"details_url":null}]
> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


