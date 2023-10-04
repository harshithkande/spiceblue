from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json 

uri = "mongodb+srv://kandeharshith70:mm1XbID9aiiF1eXb@harshithkande.dpws0gn.mongodb.net/?retryWrites=true&w=majority"

mongo = MongoClient(uri, server_api=ServerApi('1'))

app = Flask(__name__)


def verify(data):
    collection = mongo.Mydb.users
    user_details  = collection.find_one(data)
    if user_details:
        return user_details
    else:
        return False
   
def insert(data):
    collection = mongo.Mydb.users
    id  = collection.insert_one(data).inserted_id
    return jsonify(message="Document added successfully", id=str(id)), 201
   
def insert_template(data):
    collection = mongo.Mydb.template
    id  = collection.insert_one(data).inserted_id
    return jsonify(message="Document added successfully", id=str(id)), 201

def all_template():
    collection = mongo.Mydb.template
    templates  = collection.find()
    template_details = []
    for i in templates:
        template_details.append(i)
    return jsonify(message="templates", data=str(template_details)), 201
    
def get_template_data(id):
    collection = mongo.Mydb.template
    template_data  = collection.find_one(id)
    return jsonify(message="templates", data=str(template_data)), 201
    
def update_template_data(template_id, data):
    collection = mongo.Mydb.template
    template_id  = collection.update_one(template_id, data)
    return jsonify(message="templates", id=str(template_id)), 201

def delete_template_id(template_id):
    collection = mongo.Mydb.template
    template_id  = collection.delete_one(template_id)
    return jsonify(message="deleted template successfully"), 201

