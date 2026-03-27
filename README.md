# Deploying to cloudrun demo
This repository contains a sample to-do list app made in python and basic html. To remove a to-do, you need to enter the TODO_SECRET set in the system environment

## Quick steps to deploy to cloudrun
1. Make a project in google cloud console (console.cloud.google.com)
<img width="1121" height="647" alt="image" src="https://github.com/user-attachments/assets/f06ecc5e-e27a-4bf4-b79f-863128dbc6d3" />

2. Enable the required APIs (cloud build and cloud run admin) by going to the API library
<img width="1130" height="632" alt="image" src="https://github.com/user-attachments/assets/1a13c67d-e9aa-4feb-8a86-f057fb500a35" />
<img width="1234" height="685" alt="image" src="https://github.com/user-attachments/assets/6e21ee58-05ed-4c06-af56-d7d459007335" />

2. Open google cloud shell sdk and set the terminal project to that project (make sure you logged in first using gcloud auth login)
<img width="881" height="113" alt="image" src="https://github.com/user-attachments/assets/5c0a09b8-6bb9-4b6c-b25f-37c7f69d4c4e" />

* If you forgot the project id, do gcloud projects list

3. Go to the project directory, and run gcloud builds submit --tag gcr.io/<PROJECT_ID>/<NAME>:<VERSION>
<img width="1295" height="454" alt="image" src="https://github.com/user-attachments/assets/34c1214c-196e-4e4a-bbd6-b7a9736dfc98" />

Should end with something like this:
<img width="1898" height="109" alt="image" src="https://github.com/user-attachments/assets/a1e163bc-a9e3-48b9-939a-79f5b929f541" />

4. Once build is done, you can check the artifact registry, or deploy straight away

Deploying:
<img width="1059" height="604" alt="image" src="https://github.com/user-attachments/assets/3ebcd860-8249-4ab1-97b7-2c46c6c355bc" />

<img width="1056" height="609" alt="image" src="https://github.com/user-attachments/assets/49954827-c679-4bb7-9fa1-fe63c3a32d10" />

Set up the required configuration, and click create

* To set the system environment variables, it is under Containers, networking, security -> Containers -> Variables & Secrets
