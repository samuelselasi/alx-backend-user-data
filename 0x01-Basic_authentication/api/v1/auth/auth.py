#!/usr/bin/env python3
"""Module that manages API authentication"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Class that manages API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that manages authentication"""

        if path is None or excluded_paths is None or not len(excluded_paths):
            return True

        if path[-1] != '/':
            path = path + '/'

        for i in excluded_paths:
            if i.endswith('*'):
                if path.startswith(i[:1]):
                    return False

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Funtion that manages authorization header"""

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """

        return None
