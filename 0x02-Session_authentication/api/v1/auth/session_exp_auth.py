#!/usr/bin/env python3
"""Module to handle expiration for Session authentication"""
from datetime import datetime, timedelta
import os
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Class that defines attributes to handle session expiration"""

    def __init__(self):
        """Method to dinitialise attributes to handle session expiration"""

        dur = os.getenv('SESSION_DURATION')

        if dur is not None and dur.isnumeric():
            self.session_duration = int(dur)
        else:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """Method that creates a Session ID for a user"""

        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()}

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Method that returns a User ID based on a Session ID"""

        if session_id is None:
            return None

        user_session = self.user_id_by_session_id.get(session_id)

        if user_session is None:
            return None

        if self.session_duration <= 0:
            return user_session.get('user_id')

        extime = user_session.get('created_at')

        if extime is None:
            return None

        expiration_time = user_session.get(
                'created_at') + timedelta(seconds=self.session_duration)

        if expiration_time < datetime.now():
            return None

        return user_session.get('user_id')
