#!/usr/bin/env python3
"""Module handling user authentication"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


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

    def create_session(self, email: str) -> str:
        """Method to generate session id based on user email"""

        try:
            user = self._db.find_user_by(email=email)

        except NoResultFound:
            return None

        else:
            session_id = _generate_uuid()

            self._db.update_user(user.id, session_id=session_id)
            return session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """Method that returns a user based on session id"""

        try:
            user = self._db.find_user_by(session_id=session_id)

        except NoResultFound:
            return None

        else:
            return user

    def destroy_session(self, user_id: int) -> None:
        """Method that updates session ID to None based on user id"""

        try:
            self._db.update_user(user_id, session_id=None)

        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Method that takes email and returns uuid for that user"""

        try:
            user = self._db.find_user_by(email=email)

        except NoResultFound:
            raise ValueError

        token = _generate_uuid()

        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """Method that uses reset token to change password of a user"""

        try:
            user = self._db.find_user_by(reset_token=reset_token)

        except NoResultFound:
            raise ValueError

        newPwd = _hash_password(password)
        self._db.update_user(user.id, hashed_password=newPwd,
                             reset_token=None)


def _generate_uuid() -> str:
    """Function that returns a string representation of a new UUID"""

    return str(uuid.uuid4())
