from flask import Blueprint, request, jsonify
import json
import os

login_blueprint = Blueprint('login', __name__)

USER_PROFILE_FILE = '/app/database/userinfo.json'

@login_blueprint.route('/login', methods=['POST'])
def login():
    def load_user_profiles():
        """Load user profiles from the JSON file."""
        if os.path.exists(USER_PROFILE_FILE):
            try:
                with open(USER_PROFILE_FILE, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return {"users": []}
        else:
            print(f"File not found: {USER_PROFILE_FILE}")
            return None

    data = request.json
    if not data:
        return jsonify({"body": "Fill all attributes"}), 205

    username = data.get('username')  # username or email
    auth_password = data.get('password')
    print(auth_password)

    if not username or not auth_password:
        return jsonify({"body": "Fill all attributes"}), 205

    user_profiles = load_user_profiles()
    if user_profiles is None:
        return jsonify({"body": "Server Busy"}), 400

    for user in user_profiles.get('users', []):
        if user['username'] == username or user['email'] == username:
            if user['password'] == auth_password:
                return jsonify({"body": "Login Successful"}), 200
            else:
                return jsonify({"body": "Invalid Credentials"}), 400

    return jsonify({"body": "UserName or Email Doesn't Exist, please Register"}), 400
