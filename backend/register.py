from flask import Blueprint, request, jsonify
import json
import os
import bcrypt

register_blueprint = Blueprint('register', __name__)

USER_PROFILE_FILE = '/home/ec2-user/devops_session/python_cicd/heroku_application/flask_deployment/database/userinfo.json'

@register_blueprint.route('/register', methods=['POST'])
def signup():
    def load_user_profiles():
        """Load existing user profiles from the JSON file."""
        if os.path.exists(USER_PROFILE_FILE):
            try:
                with open(USER_PROFILE_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error loading JSON file: {e}")
                return {"users": []}
        else:
            print(f"File not found: {USER_PROFILE_FILE}")
            return {"users": []}

    def save_user_profiles(data):
        """Save user profiles to the JSON file."""
        try:
            with open(USER_PROFILE_FILE, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving user profiles: {e}")
            raise

    try:
        data = request.json
        if not data:
            return jsonify({"message": "Invalid request data"}), 400

        username = data.get('username')
        email = data.get('email')
        hashed_password = data.get('password')

        # Validate required fields
        if not username or not email or not hashed_password:
            return jsonify({"message": "Missing required fields"}), 400

        # Load existing profiles
        user_profiles = load_user_profiles()
        if user_profiles is None:
            return jsonify({"message": "Server busy, please try again later"}), 500

        # Check for existing username or email
        for user in user_profiles['users']:
            if user['username'] == username or user['email'] == email:
                return jsonify({"message": "Username or email already exists"}), 400

        # Hash the password before storing
        #hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Create the new user profile
        new_user = {
            "username": username,
            "email": email,
            "password": hashed_password,  # Store hashed password
            "full_name": data.get('full_name', ''),
            "phone_number": data.get('phone_number', ''),
            "dob": data.get('dob', ''),
            "is_active": True
        }

        # Append the new user and save
        user_profiles['users'].append(new_user)
        save_user_profiles(user_profiles)

        return jsonify({"message": "User registered successfully!"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Server busy, please try again later"}), 500
