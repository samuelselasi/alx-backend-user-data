#!/usr/bin/env python3
"""Module containing flask app"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """Endpoint that returns a JSON payload"""

    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Endpoint to register a user"""

    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200

    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Endpoint to login a user with email and password"""

    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password) is False:
        abort(401)

    session_id = AUTH.create_session(email)
    res = jsonify({'email': email, 'message': 'logged in'})

    res.set_cookie('session_id', session_id)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
