# app.py
from flask import Flask
from flask_cors import CORS
from backend.register import register_blueprint
from backend.login import login_blueprint

# Create Flask app
app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Hello World</h1>"

# Configure CORS
CORS(app, supports_credentials=True)

# Register blueprints
app.register_blueprint(register_blueprint, url_prefix='/auth')
app.register_blueprint(login_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
