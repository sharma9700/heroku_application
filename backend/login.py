from flask import Blueprint, request, jsonify
import json
import os
import bcrypt

login_blueprint = Blueprint('login', __name__)


USER_PROFILE_FILE = '/flask_deployment/database/userinfo.json'
def load_user_profiles():
    if os.path.exists(USER_PROFILE_FILE):
        with open(USER_PROFILE_FILE, 'r') as f:
            print(f)
            return json.load(f)
    return {"users": []}
    

@login_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    print(data)
    username = data.get('username')
    #email = data.get('email')
    auth_password = data.get('password')

    # Check if any required field is missing
    if not (username or email) or not auth_password:
        return jsonify({"body": "Fill all attributes"}), 205
    else:
        user_profiles = load_user_profiles()
        #print(user_profiles)
        user_found = False
        #print(user_profiles['users'])
        for user in user_profiles['users']:
            print(user)
            if user['username'] == username or user['email'] == username:
                print(user['username'])
                if user['password'] == auth_password:
                    return jsonify({"body": "Login Successful"}), 200
                else:
                    return jsonify({"body": "Invalid Credentials"}), 400
            else:
                print(user['email'])
                print(' != ')
                print(username)

    return jsonify({"body": "UserName or Email Doesn't Exist, please Register"}), 400

            
            
            

