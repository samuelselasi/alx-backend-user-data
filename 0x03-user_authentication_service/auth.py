#!/usr/bin/env python3
"""Module handling user authentication"""
import bcrypt


def _hash_password(password: str) -> str:
    """Function to encodes password in string to bytes"""

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
