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


Step 3:
create a config folder to define database configuration to connect to mongodb 
create a model folder to define the pydantic model 


Step 4:
create a schema folder to define serializers on how our data is represented
create route folder to define different routes. we define the CRUD api operation

How to use:
=================
Run uvicorn api:app
open http://127.0.0.1:8000/docs
