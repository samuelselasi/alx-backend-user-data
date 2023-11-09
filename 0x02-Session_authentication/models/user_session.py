#!/usr/bin/env python3
"""Module that handles user session"""
from models.base import Base


class UserSession(Base):
    """Class that defines attributes for user session"""

    def __init__(self, *args: list, **kwargs: dict):
        """Function that initializes UserSession instances"""

        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
