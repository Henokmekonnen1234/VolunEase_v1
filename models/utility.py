#!/usr/bin/python3
"""
Module utility.py
This file is used to utilities
"""

from datetime import datetime, timedelta
from uuid import uuid4
from models import storage
import bcrypt
import jwt


def encrypt(value=None):
    """This method is used to encrypt strings"""
    if value:
        result = bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        return result
    else:
        return bcrypt.hashpw(b"None", bcrypt.gensalt()).decode("utf-8")

def decrypt(user_input=None, stored_hash=None):
    """This method will check if the user input matches the stored hash"""
    if user_input and stored_hash:
        return bcrypt.checkpw(user_input.encode("utf-8"), stored_hash.encode("utf-8"))
    else:
        return False
    
def jwt_encode(value=None, secret=None):
    """This method is used to encode or generate JWT"""
    if value and secret:
        return jwt.encode({"id": value, 'exp': datetime.utcnow() +
                           timedelta(10)}, secret,
                           algorithm="HS256")
    else:
        return None

def jwt_decode(value=None, secret=None):
    """This method will decode the JWT"""
    from api.v1.app import app
    if value and secret:
        tokens = jwt.decode(value, secret, algorithms=['HS256'])
        org_id = tokens["id"]
        return org_id
    else:
        return value
    
def taken_value(cls, **kwargs):
    """This method will check if the value is present in the saved 
    object
    """
    obj = None
    if kwargs:
        for key, value in kwargs.items():
            if key == "name":
                obj = storage.filter(cls, key, value)
                if obj:
                    return f"{key} already present, change your {key}"
            elif key == "email":
                obj = storage.filter(cls, key, value)
                if obj:
                    return f"{key} already present, change your {key}"
            elif key == "phone_no":
                obj = storage.filter(cls, key, value)
                if obj:
                    return f"{key} already present, change your {key}"
            elif key == "website":
                obj = storage.filter(cls, key, value)
                if obj:
                    return f"{key} already present, change your {key}"
            elif key == "description":
                obj = storage.filter(cls, key, value)
                if obj:
                    return f"{key} already present, change your {key}"
        return False
    else:
        return f"No value passed"