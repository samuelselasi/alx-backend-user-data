#!/usr/bin/env python3
"""Module that manages API authentication"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Class that manages API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that manages authentication"""

        return False

    def authorization_header(self, request=None) -> str:
        """Funtion that manages authorization header"""

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """

        return None
