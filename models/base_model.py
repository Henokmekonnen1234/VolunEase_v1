#!/usr/bin/python3
"""
Module base_model.py

This module is the base file for saving and to change it to dictionary
file.
"""

from datetime import datetime
from models import storage
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import decralative_base
from uuid import uuid4

time = "%Y-%m-%dT%H:%M:%S.%f"
Base = decralative_base()


class BaseModel:
    """This class is the base for all aother classes contain method for
       saving and changing to dictionary file

    Attributes:
        id (str): indentifying each object uniquely
        created_date (datetime): store created date of object
        update_date (datetime): store update date of object
    """
    
    id = Column(String(60), primary_key=True, nullable=False,
                unique=True)
    created_date = Column(DateTime, default=datetime.utcnow,
                          nullable=False)
    updated_date = Column(DateTime, default=datetime.utcnow,
                          nullable=False)
    
    def __init__(self, *args, **kwargs):
        """this method will initialize the basemodel"""
        if "id" not in kwargs.keys() and "updated_date"\
            not in kwargs.keys():
            self.id = uuid4()
            self.created_date = datetime.utcnow()
            self.updated_date = datetime.utcnow()
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def save(self):
        """This will send the object to be saved"""
        storage.new(self)
        storage.save()

    def to_dict(self):
        """This method will change class instance to dictionary"""
        to_dict = self.__dict__.copy()
        to_dict["__class__"] = self.__class__.__name__
        if "created_at" in to_dict:
            to_dict["created_at"] = to_dict["created_at"].strftime(time)
        if "updated_at" in to_dict:
            to_dict["updated_at"] = to_dict["updated_at"].strftime(time)
        if "_sa_instance_state" in to_dict:
            del to_dict["_sa_instance_state"]
        if "password" in to_dict:
            del to_dict["password"]
        return to_dict         

    def str():
        """This method will be used to represent the class in string
        format
        """
        
    def delete():
        pass