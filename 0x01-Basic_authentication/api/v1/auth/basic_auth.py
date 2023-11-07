#!/usr/bin/env python3
"""Module that manages API authentication"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class that manages basic API authentication"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Method that  returns Base64 part of Authorization header"""

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        base = authorization_header.split(' ')
        return base[1]
