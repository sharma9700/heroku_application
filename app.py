# app.py
from flask import Flask, render_template
from flask_cors import CORS
from backend.register import register_blueprint
from backend.login import login_blueprint

# Create Flask app
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
	return render_template("app/frontend/index.html")

# Configure CORS
CORS(app, supports_credentials=True)

# Register blueprints
app.register_blueprint(register_blueprint, url_prefix='/auth')
app.register_blueprint(login_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
