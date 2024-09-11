# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory user data (replace with a database in a real app)
users = []

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Simple authentication check
    user = next((user for user in users if user['email'] == email and user['password'] == password), None)

    if user:
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Check if the user already exists
    if any(user['email'] == email for user in users):
        return jsonify({"message": "User already exists!"}), 400

    users.append({"email": email, "password": password})
    return jsonify({"message": "User registered successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
