#!/usr/bin/env python3
"""Module handling user authentication"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> str:
    """Function to encodes password in string to bytes"""

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method that returns a User object based on email and password"""

        try:
            user = self._db.find_user_by(email=email)

        except NoResultFound:
            userPwd = _hash_password(password)
            user = self._db.add_user(email, userPwd)

            return user

        else:
            raise ValueError('User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Method that checks if password is correct and returns a boolean"""

        try:
            u = self._db.find_user_by(email=email)

        except NoResultFound:
            return False

        else:
            return bcrypt.checkpw(password.encode('utf-8'), u.hashed_password)
