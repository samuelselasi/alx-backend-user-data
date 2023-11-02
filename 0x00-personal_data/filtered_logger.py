#!/usr/bin/env python3
"""Module containing functions to obfuscate log messages"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function that returns the log message obfuscated"""
    for i in fields:
        message = re.sub(f'{i}=.*?{separator}', f'{i}={redaction}{separator}',
                         message)
    return message
