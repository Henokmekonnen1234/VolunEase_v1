#!/usr/bin/python3
"""
Module base_model.py

This module is the base file for saving and to change it to dictionary
file.
"""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import decralative_base


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

    def save():
        pass

    def to_dict():
        pass

    def str():
        pass

    def delete():
        pass