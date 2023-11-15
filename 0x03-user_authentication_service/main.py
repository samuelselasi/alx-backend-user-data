#!/usr/bin/env python3
"""Main module to test user authentication in Flask app"""
import requests

URL = 'http://localhost:5000'


def register_user(email: str, password: str) -> None:
    """Method to test user registration with email and password"""

    user = {"email": email, "password": password}
    res = requests.post(f'{URL}/users', user)

    assert res.status_code == 201


def log_in_wrong_password(email: str, password: str) -> None:
    """Method to test login with wrong password"""

    user = {"email": email, "password": password}
    res = requests.post(f'{URL}/sessions', user)

    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """Method to test login"""

    user = {"email": email, "password": password}
    res = requests.post(f'{URL}/sessions', user)

    assert res.status_code == 200


def profile_unlogged() -> None:
    """Method to test logged out user"""

    session = {"session_id": ""}
    res = requests.get(f'{URL}/profile', session)
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """Method to log access data of logged in user"""

    data = {"session_id": session_id}
    res = requests.get(f'{URL}/profile', data)

    assert res.status_code == 200


def log_out(session_id: str) -> None:
    """Method to log out a user with session id"""

    data = {"session_id": session_id}
    res = requests.delete(f'{URL}/sessions', data)

    assert res.status_code == 204


def reset_password_token(email: str) -> str:
    """Method to test generation of reset password token"""

    data = {"email": email}
    res = requests.post(f'{URL}/reset_password', data)

    assert response.status_code == 200

    # reset_token = res.json().get("reset_token")

    # assert res.status_code == 200, "Reset token generated"


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Method to test password update with form data"""

    data = {
        "email": email, "reset_token": reset_token,
        "new_password": new_password}

    res = requests.put(f'{URL}/reset_password', data)

    assert res.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
