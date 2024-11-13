from flask import Blueprint, request, jsonify
import json
import os
import bcrypt

register_blueprint = Blueprint('register', __name__)

USER_PROFILE_FILE = '/database/userinfo.json'

# Load existing user profiles from JSON file
def load_user_profiles():
    if os.path.exists(USER_PROFILE_FILE):
        with open(USER_PROFILE_FILE, 'r') as f:
            print(f)
            return json.load(f)
    return {"users": []}

# Save user profiles to JSON file
def save_user_profiles(data):
    with open(USER_PROFILE_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@register_blueprint.route('/register', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    print(username)
    email = data.get('email')
    print(email)
    auth_password = data.get('password')
    print(auth_password)
    # Load existing profiles
    user_profiles = load_user_profiles()
    print(user_profiles)
    print(data)

    # Check if the user already exists
    for user in user_profiles['users']:
        if user['username'] == username or user['email'] == email:
            return jsonify({"message": "Username or email already exists"}), 400

    # Hash the password
    # Create new user profile
    new_user = {
        "username": username,
        "email": email,
        "password": auth_password,  # Store hashed password as string
        "full_name": data.get('full_name', ''),
        "phone_number": data.get('phone_number', ''),
        "dob": data.get('dob', ''),
        "is_active": True
    }
    
    # Append new user to existing profiles
    try:
        user_profiles['users'].append(new_user)
        save_user_profiles(user_profiles)
        print(save_user_profiles)
        print(save_user_profiles.users)
    except Exception as e:
        print(e)
    
    return jsonify({"message": "User registered successfully!"}), 200
