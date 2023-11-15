#!/usr/bin/env python3
"""Module containing flask app"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Endpoint to logout a user with session id from cookies"""

    session_id = request.cookies.get('session_id')

    if session_id is None:
        return jsonify({"error": "Session ID not found"}), 403

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        return jsonify({"error": "User not found"}), 403

    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """Endpoint that returns a users email from session id in cookie"""

    session_id = request.cookies.get('session_id')

    if session_id is None:
        return jsonify({"error": "Session ID not found"}), 403

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        return jsonify({"error": "User not found"}), 403

    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """Endpoint that generates a token for a user based on email"""

    try:
        email = request.form.get('email')
        token = AUTH.get_reset_password_token(email)

        return jsonify({"email": email, "reset_token": token}), 200

    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """Endpoint that updates password with email and token from form data"""

    email = request.form.get('email')
    token = request.form.get('reset_token')
    password = request.form.get('new_password')

    try:
        AUTH.update_password(token, password)

    except Exception as err:
        return jsonify({"error": str(err)}), 403

    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
