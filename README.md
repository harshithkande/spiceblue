Flask and MongoDB RESTful API with User Authentication using JWT

This project demonstrates the creation of a RESTful API using Flask and MongoDB, along with user authentication using JWT (JSON Web Token). The API has three endpoints for user registration, user login, and template management.

Prerequisites

Python 3.x

Postman

MongoDB Atlas account (for free MongoDB hosting with 512MB size)

To connect to my mongoDB cluster we need to add your personal ip address in harhithkande mongodb database.

Setup

I have hosted my project using render application.

Please follow the below steps to access(response) the implemented endpoints.

1.First we need to register to login so 

use this url to register:  https://spiceblue-test.onrender.com/register , method = POST 

Request Body:
{
    "first_name": "Harshith",
    "last_name": "Kande",
    "email": "Harshith.Kande.doe@example.com",
    "password": "password"
}

Response: 201
{
    "message": "User registered successfully",
    "user_id": "(<Response 74 bytes [200 OK]>, 201)"
}

2. After resigiter in above step use the below url to login.

Login url: https://spiceblue-test.onrender.com/login.

Request Body:
{
"email" : "Harshith.Kande.doe@example.com",
"password" : "password"
} 

Response: 200
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjU3MDY0MSwianRpIjoiMzhiMDY3MGQtM2FkNy00YzAyLTkxNWUtYjZiZTg3MmQ3MzhmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY1MWY5YzY2NDIyYzU1ZTdiZjIxZjlhMSIsIm5iZiI6MTY5NjU3MDY0MSwiZXhwIjoxNjk2NTcxNTQxfQ.C1M0RquGtnvwL1rMTIXK_qXThvkPMbXJOLToCedzvXs"
}

Note:
1. I haven't consider the validation for password feild.
2. This access token is used as the authorisation for the all endpoint related to templates.

3.a
For inserting new template in mongodb tempalte table use below url

URL: https://spiceblue-test.onrender.com/template,Method: POST

Headers:
json
Copy code
{
    'Authorization': 'Bearer <access_token>',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

Request Body:
json

  {
                "template_name": "harshith",
                "subject": "tets",
                "body": "created template"
} 

Response: 201

{
    "id": "651fa3e99481a3286321f9a1",
    "message": "Document added successfully"
}

3.b Get All Template present in my mongodb 
URL: https://spiceblue-test.onrender.com/template, Method: GET

Headers:
json
{
    'Authorization': 'Bearer <access_token>',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

Body:
json

response:
{
    "data": "[{'_id': ObjectId('651cb6c593aa31be05c39c18'), 'template_name': 'harshith', 'subject': 'tets', 'body': 'updataed', 'customer_id': '651c46dcadf1fca4a03d0ad9'}, {'_id': ObjectId('651cb70893aa31be05c39c19'), 'template_name': 'harshith123', 'subject': 'test123', 'body': 'created template', 'customer_id': '651c46dcadf1fca4a03d0ad9'}]",
    "message": "templates"
}

3.c Get Single Template with tempalte_id
URL: https://spiceblue-test.onrender.com/template/<template_id>
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

response:
{
    "data": "{'_id': ObjectId('651cb6c593aa31be05c39c18'), 'template_name': 'harshith', 'subject': 'tets', 'body': 'updataed', 'customer_id': '651c46dcadf1fca4a03d0ad9'}",
    "message": "templates"
}

3.d Update Single Template
URL: https://spiceblue-test.onrender.com/template/<template_id>
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


3.e Delete Single Template
URL: https://spiceblue-test.onrender.com/template/<template_id>
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


Note: for all endpoint elated to template use the access token which we generated in login endpoint.
