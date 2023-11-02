#!/usr/bin/env python3
"""Module containing password hashing methods"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Function returns salted and hashed password taken in string format"""

    encrypted = password.encode()
    hashed_password = bcrypt.hashpw(encrypted, bcrypt.gensalt())
    return hashed_password
