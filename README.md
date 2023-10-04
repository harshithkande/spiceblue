Flask and MongoDB RESTful API with User Authentication using JWT

This project demonstrates the creation of a RESTful API using Flask and MongoDB, along with user authentication using JWT (JSON Web Token). The API has three endpoints for user registration, user login, and template management.

Prerequisites

Python 3.x

Postman

MongoDB Atlas account (for free MongoDB hosting with 512MB size)

To connect to my mongoDB cluster we need to add your personal ip address in harhithkande mongodb database.

Setup

Clone the repository:

bash
Copy code

git clone https://github.com/harshithkande/spiceblue.git


Create virtual environment with name spiceblue 
bash 
copy code
python3 -m venv spiceblue
Here venv is created with name spiceblue

To activate spiceblue venv 
bash 
copy code
source spiceblue/bin/activate

Install dependencies:

To install all requirements to run the application
bash
Copy code

pip install -r requirements.txt

Run the Application
bash
Copy code

python3 app.py


Your Flask app will be hosted on a local server e.g.,(http://127.0.0.1:5000).

API Endpoints
1. Register
URL: http://127.0.0.1:5000/register
Method: POST


Headers:
json
Copy code
{
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


Body:
json
Copy code
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "securepassword"
}


2. Login
URL: http://127.0.0.1:5000/login
Method: POST


Headers:
json
Copy code
{
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


Body:
json
Copy code
{
    "email": "john.doe@example.com",
    "password": "securepassword"
}

response:
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjM4MzgyMywianRpIjoiODBmYTQ4YWQtYWYyZS00ZjIyLWE0MDUtZWFjZDM1ZmQ3Yjg5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY1MWM0NmRjYWRmMWZjYTRhMDNkMGFkOSIsIm5iZiI6MTY5NjM4MzgyMywiZXhwIjoxNjk2Mzg0NzIzfQ.iKOKb3V3tgH9JOhZ8RxzWO-8MmTEX7FbignKm3jBDao"
}



3. Template CRUD

From here on use the access token that generated by login endpoint through JWT

3.1 Insert new Template
URL: http://127.0.0.1:5000/template
Method: POST

Headers:
json
Copy code
{
    'Authorization': 'Bearer <access_token>',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

Body:
json
Copy code

  {
                "template_name": "harshith",
                "subject": "tets",
                "body": "created template"
    } 

reponse:
{
    "id": "651cc4c43016efe6972303c5",
    "message": "Document added successfully"
}

3.2 Get All Template
URL: http://127.0.0.1:5000/template
Method: GET

Headers:
json
Copy code
{
    'Authorization': 'Bearer <access_token>',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
Body:
json
Copy code

response:
{
    "data": "[{'_id': ObjectId('651cb6c593aa31be05c39c18'), 'template_name': 'harshith', 'subject': 'tets', 'body': 'updataed', 'customer_id': '651c46dcadf1fca4a03d0ad9'}, {'_id': ObjectId('651cb70893aa31be05c39c19'), 'template_name': 'harshith123', 'subject': 'test123', 'body': 'created template', 'customer_id': '651c46dcadf1fca4a03d0ad9'}]",
    "message": "templates"
}

3.3 Get Single Template
URL: http://127.0.0.1:5000/template/<template_id>
Method: GET

Headers:
json
Copy code
{
    'Authorization': 'Bearer <access_token>',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

Body:
json
Copy code
{}


response:
{
    "data": "{'_id': ObjectId('651cb6c593aa31be05c39c18'), 'template_name': 'harshith', 'subject': 'tets', 'body': 'updataed', 'customer_id': '651c46dcadf1fca4a03d0ad9'}",
    "message": "templates"
}


3.4 Update Single Template
URL: http://127.0.0.1:5000/template/<template_id>
Method: PUT

Headers:
json
Copy code
{
    'Authorization': 'Bearer <access_token>',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

Body:
json
Copy code
{
    "template_name": "Updated Template",
    "subject": "Updated subject",
    "body": "Updated body content."
}

response:
{
    "id": "<pymongo.results.UpdateResult object at 0x7efe04340100>",
    "message": "templates"
}

3.5 Delete Single Template
URL: http://127.0.0.1:5000/template/<template_id>
Method: DELETE

Headers:
json
Copy code
{
    'Authorization': 'Bearer <access_token>',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

Body:
json
Copy code
{}

response:
{
    "message": "deleted template successfully"
}
