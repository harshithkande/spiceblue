from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from db import verify, insert, insert_template, all_template, get_template_data, update_template_data, delete_template_id
from bson import ObjectId

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password = data['password']
    email_details = {'email': email}
    db = 'Mydb'
    collection_name = 'users'
    if verify(email_details):
        return jsonify({'message': 'User already exists'}), 400
    user_id = insert({'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password})
    return jsonify({'message': 'User registered successfully', 'user_id': str(user_id)}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    details = {'email': email, 'password': password}
    user = verify(details)
    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401
    access_token = create_access_token(identity=str(user['_id']))
    return jsonify({'access_token': access_token}), 200

@app.route('/template', methods=['POST'])
@jwt_required()
def create_template():
    current_user = get_jwt_identity()
    data = request.get_json()
    data['customer_id'] = current_user
    return insert_template(data)


@app.route('/template', methods=['GET'])
@jwt_required()
def get_all_templates():
    current_user = get_jwt_identity()
    return all_template()

@app.route('/template/<template_id>', methods=['GET'])
@jwt_required()
def get_template(template_id):
    template_id = request.args.get('template_id')
    template_data = get_template_data(template_id)
    return template_data

@app.route('/template/<template_id>', methods=['PUT'])
@jwt_required()
def update_template(template_id):
    current_user = get_jwt_identity()
    data = request.get_json()
    updated_data_json =   {
                '$set': {'template_name': 'hellooo'}
                }
    template_id_json = {'_id': ObjectId(template_id)}
    return update_template_data(template_id_json, updated_data_json)
    
@app.route('/template/<template_id>', methods=['DELETE'])
@jwt_required()
def delete_template(template_id):
    current_user = get_jwt_identity()
    template_id_json = {'_id': ObjectId(template_id)}
    return delete_template_id(template_id_json)

if __name__ == '__main__':
    app.run(debug=True)
