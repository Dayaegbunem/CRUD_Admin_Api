# CRUD_Admin_Api
Abstract
A simple CRUD api backend using Mongodb as the database.

Step 1:
Create a mongoDb account, startup a database cluster
An ec2 instance running on AWS is required
Install these dependencies, if you do not have already:
Python, aws cli, vscode, FastAPI, uvicorn, Panda, Pymongo, pymongo[srv]

Step 2:
On VScode create a variable folder 'api.py' and run the code 'uvicorn api:app' to open development server on a local host port 8000.
![dev_server](https://user-images.githubusercontent.com/126528702/227085824-65e0f6d4-42d0-4a57-af71-186cad0d120e.PNG)


![crud_Op](https://user-images.githubusercontent.com/126528702/227085863-2e63601a-087a-4605-9d46-4bdf359257b2.PNG)


Step 3:
create a config folder to define database configuration to connect to mongodb 
create a model folder to define the pydantic model 


Step 4:
create a schema folder to define serializers on how our data is represented
create route folder to define different routes. we define the CRUD api operation

![crud_Op](https://user-images.githubusercontent.com/126528702/227085967-cf46788d-f972-409f-9692-3f1af660a53b.PNG)


![crud_read](https://user-images.githubusercontent.com/126528702/227085981-90f8a475-66d9-48d9-94c5-d9d048d86cdd.PNG)

How to use:
=================
Run uvicorn api:app
open http://127.0.0.1:8000/docs
