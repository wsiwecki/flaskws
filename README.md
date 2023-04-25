# Overview

<TODO: complete this with an overview of your project>

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project

https://trello.com/invite/b/HPVtYyJR/ATTI53b8619f331e536c95f4123178f9ba4d301ED1B4/azure-devops-ci-cd

* A link to a spreadsheet that includes the original and final project plan>:

https://docs.google.com/spreadsheets/d/1LD9J6WBjs48r34Q5RipeMulNv3CYptiQk0NJBGMFYB0/edit?usp=sharing

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

* ![00_diagram](https://user-images.githubusercontent.com/58573764/234246730-23d60c6e-aa59-4206-94b4-e4702173fd3c.jpg)


<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service:

First we have to create ne Web App with seting source on GitHub - our project:

![06_screenhot_Webb_app_Settings](https://user-images.githubusercontent.com/58573764/234284133-a91b668f-c0fa-48bc-8c52-74b75e350eca.jpg)
![06_screenhot_Webb_app_Settings](https://user-images.githubusercontent.com/58573764/234284198-9875de9a-7481-4355-a27c-7da8673950a1.jpg)


* Project cloned into Azure Cloud Shell

We can also clone repository of project to our Azure Clound Shell, buy execute git cone - path copied from my repository:

```bash
git clone git@github.com:wsiwecki/azure-devops.git
```

![01_sceenshot_clone_project_to_Azur_Cloud_Shell](https://user-images.githubusercontent.com/58573764/234284888-2c661324-6b64-4a73-bb11-a306a7500209.jpg)


* Passing tests that are displayed after running the `make all` command from the `Makefile`

Result of runing make all (2 screens) :

![02_sceenshot_make_all_part_01](https://user-images.githubusercontent.com/58573764/234285060-f3e93c50-e690-4142-9fa6-b0c687bae30c.jpg)

![02_sceenshot_make_all_part_02](https://user-images.githubusercontent.com/58573764/234285114-f988681f-22e8-4cac-98d9-cc7f357ed217.jpg)

* Output of a test run

![image](https://user-images.githubusercontent.com/58573764/234285735-22699a4a-4a1c-46fe-bb2c-9822b9003857.png)


* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

I have succesfully buid and deploy project by GitHub Actions (belowed screenshot) but have some authentication problems with running Azure Pipeline.

I'm using my copmany account in Azure and have no all possible access to deploy application. Pipeline is configured correctly and connection to Azure works, but I can only authentication by Managed Identity Authentication with no full access.

![image](https://user-images.githubusercontent.com/58573764/234287670-d1bcd6bc-63ef-4912-aded-e97ba62a0f8a.png)

In this case I'm sure that I can successfully deploy (setup CI/CD) using GitHub Actions, what I can show as resolve this time:

![image](https://user-images.githubusercontent.com/58573764/234288063-5c09d8f2-01ce-4daf-865e-59a2882efa83.png)


* Running Azure App Service from Azure Pipelines automatic deployment
Sceen shot of result deploing:

![image](https://user-images.githubusercontent.com/58573764/234291602-a87d0bc7-e474-45bf-968f-e4b0e7b7f36b.png)

and running Azure App Service:

![image](https://user-images.githubusercontent.com/58573764/234291847-dae27cf7-a654-4f58-ae64-281bd97d2b84.png)


* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).

This is my output:

```bash
wojciech_siwecki [ ~/flaskws ]$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[2.431574790057212]}
```

* Output of streamed log files from deployed application

![image](https://user-images.githubusercontent.com/58573764/234288582-c1ac0c95-1a4e-4898-9e5e-1794fb582d3b.png)

![image](https://user-images.githubusercontent.com/58573764/234288923-1db615d9-4439-426a-bbcc-e1dd775c1b52.png)


## Enhancements

<TODO: A short description of how to improve the project in the future>

I am to receive new kind of account with admin access on my own subscription, and can move this project to the new subscription.
But most important is my pararell project - in which I'm using Azure Pipeline with Ansible plugins. In this project I standarized
and configured almost 20 servers with similar running services. I see that it is very usefully, fast in working and readable by others solutions.

## Demo 

<TODO: Add link Screencast on YouTube>


