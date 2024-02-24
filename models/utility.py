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
import os

UPLOAD_FOLDER = "/home/drogo/ALX/VolunEase_v1/web_flask/static/images/uploaded"

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
    try:
        if value and secret:
            tokens = jwt.decode(value, secret, algorithms=['HS256'])
            org_id = tokens["id"]
            return org_id
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

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
                    return f"Phone number already present, change your phone number"
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

def get_unique_filename(filename):
    """This method will generate a new name for the file"""
    file_extension = os.path.splitext(filename)[1]
    unique_filename = str(uuid4()) + file_extension
    return unique_filename

def save_file(file):
    """This method will save the file and return the path"""
    if file:
        file_name = get_unique_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        file.save(file_path)
        return f"/uploaded/{file_name}"
    else:
        return None

def delete_file(file):
    """This methos will delete the file"""
    file_path = os.path.join(UPLOAD_FOLDER, file)
    if os.path.exists(file_path):
        os.remove(file_path)

def check_token(token):
    """Check if the token present"""
    from api.v1.app import app
    if token:
        obj_id = jwt_decode(token, app.config["SECRET_KEY"])
        return obj_id
    else:
        return None