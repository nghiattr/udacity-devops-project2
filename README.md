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


## Link of the Trello board

https://trello.com/b/ormxYoYZ/nghiaproject

[![Flask application test with Github Actions](https://github.com/nghiattr/udacity-devops-project2/actions/workflows/pylint.yml/badge.svg)](https://github.com/nghiattr/udacity-devops-project2/actions/workflows/pylint.yml)

