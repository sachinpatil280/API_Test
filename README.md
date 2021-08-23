# API_Test

## Description
API_Test uses python 3.xx version with requests library for API automation testing. Pytest framework is used to run test cases.

## Project Structure
Here you can find a short description of main directories, and it's content.
- helper : This folder contains the logical code for taking actions on Endpoint.
- Reports : This folder will have reports generated after test executions.
- resources : This folder has requirements.txt file for installing dependenent packages and config.ini and config.yaml file for test data storing.
- tests : This folder will hold set of test cases to be executed.
- utilities : This folder has reusable codes.
- run.cmd - This file is configured to run test cases with "regression" marker, user can change it as per requirements.

## Getting Started

You need to install packages using pip according to requirements.txt file.
Navigate to "resources" folder and run the command below in terminal:
```
$ pip install -r requirements.txt
```

## Run Automated Tests
To run test cases with "regression" marker, navigate to root folder of project and use run.cmd file.


#### Future Release Plan
1. Data reading utility from csv file.
2. Implmenting CI-CD using jenkins.