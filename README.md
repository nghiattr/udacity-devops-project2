[![Flask application test with Github Actions](https://github.com/nghiattr/udacity-devops-project2/actions/workflows/pylint.yml/badge.svg)](https://github.com/nghiattr/udacity-devops-project2/actions/workflows/pylint.yml)


# Udacity Project 2: Building a CI/CD Pipeline
test
## Overview & Architectural Diagram

Purpose of this project is build and deploy a Flask Webapp based on several tools: Github, Github Action, Azure ADO, Azure pipeline.

![Architectural Diagram](./image/1.png)

## How to running this Python project (Flask)

1. Create the virtual environment using python
```bash
python3 -m venv flask-ml-azure
source flask-ml-azure/bin/activate
```

2. Install dependencies in requirement.txt file
```bash
make install
```

3.1 Start webapp in local
```bash
python3 app.py
```


4.1 In a separate shell run: `./make_prediction.sh`


3.2 Create a Azure Web App service in Azure cloud shell *Note: replace "< yourappname >" before executing.
```bash
./commands.sh
```


4.2 In a separate shell run: `./make_predict_azure_app.sh`
*Note: replace "< yourappname >" before executing.

## Step by step to create a CICD pipline

1. Create a Azure Devops Organization

![1](./image/4.png)


![1](./image/5.png)

2. Create a Git repository by import the Github repo

![1](./image/6.png)


![1](./image/7.png)


3. Create a Agent pools and Agent VM for Azure pipeline


Create a access token for Agent can connect to the Pools


![1](./image/10.png)


Create pools


![1](./image/8.png)


Create agent


![1](./image/9.png)



SSH to the VM which is the agent and run the scripts above


![1](./image/11.png)


4. Create a Service connections 


![1](./image/12.png)


![1](./image/13.png)


![1](./image/14.png)


![1](./image/15.png)


5. Create a Azure Pipeline


![1](./image/16.png)


6. Trigger the pipeline to build & deploy Flask application into Azure Web App Service


![1](./image/17.png)


Grant the permission for pipeline


![1](./image/18.png)


Check rsult:


![1](./image/19.png)


For more detai please access the Video links in "Demo links" part


## Link of the Trello board


https://trello.com/b/ormxYoYZ/nghiaproject


## Continuous Integration


A screenshot showing the project cloned into Azure Cloud Shell:
![clone](./image/21.png)


A screenshot showing the passing tests that are displayed after running the make all command from the Makefile and output of a test run:
![makefile](./image/20.png)




## Continuous Delivery


Locust: 
```bash
locust -f locustfile.py
```

Result:


![clone](./image/22.png)


![clone](./image/23.png)


and the report: locust-report.html


## Demo Links:


Github Action: 


CICD: 

