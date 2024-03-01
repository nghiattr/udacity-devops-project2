[![Flask application test with Github Actions](https://github.com/nghiattr/udacity-devops-project2/actions/workflows/pylint.yml/badge.svg)](https://github.com/nghiattr/udacity-devops-project2/actions/workflows/pylint.yml)


# Udacity Project 2: Building a CI/CD Pipeline


## Overview & Architectural Diagram

The purpose of this project is to build and deploy a Flask Webapp using various tools such as GitHub, GitHub Actions, Azure ADO, and Azure Pipeline.

![Architectural Diagram](./image/1.png)

## Running the Python Flask Project

1. Create a virtual environment using Python:
```bash
python3 -m venv flask-ml-azure
source flask-ml-azure/bin/activate
```

2. Install dependencies from the `requirements.txt` file:
```bash
make install
```

3.1 Start the web application locally:
```bash
python3 app.py
```


4.1 In a separate shell, run: `./make_prediction.sh`


3.2 Create an Azure Web App service in Azure Cloud Shell (Note: replace "< yourappname >" before executing):
```bash
./commands.sh
```


4.2 In a separate shell, run: `./make_predict_azure_app.sh` (Note: replace "< yourappname >" before executing).


## Step by step to create a CICD pipline

1. Create an Azure DevOps Organization:

![1](./image/4.png)


![1](./image/5.png)

2. Import the GitHub repository to create a Git repository:

![1](./image/6.png)


![1](./image/7.png)


3. Set up Agent pools and Agent VMs for Azure Pipeline:


Create an access token for agents to connect to the pools.


![1](./image/10.png)


Create pools.


![1](./image/8.png)


Create agents.


![1](./image/9.png)



SSH to the VM, which acts as the agent, and execute the provided scripts.


![1](./image/11.png)


4. Create Service connections:


![1](./image/12.png)


![1](./image/13.png)


![1](./image/14.png)


![1](./image/15.png)


5. Set up an Azure Pipeline:


![1](./image/16.png)


6. Trigger the pipeline to build & deploy the Flask application to Azure Web App Service:


![1](./image/17.png)


Grant permission for the pipeline:


![1](./image/18.png)


Check the result:


![1](./image/19.png)


For more details, please refer to the video links in the "Demo Links" section.


## Link to the Trello Board


[Trello Board Link](https://trello.com/b/ormxYoYZ/nghiaproject)


## Continuous Integration


A screenshot demonstrating the project cloned into Azure Cloud Shell:
![clone](./image/21.png)


A screenshot showing the passing tests displayed after running the make all command from the Makefile, along with the output of a test run:
![makefile](./image/20.png)


## Continuous Delivery


To run Locust:
```bash
locust -f locustfile.py
```

Result:


![clone](./image/22.png)


![clone](./image/23.png)


And the report: `locust-report.html`


## Demo Links:


[Github Action](https://youtu.be/FIfIcomB-Ak)


[CICD](https://youtu.be/NnCFK7AULq0)