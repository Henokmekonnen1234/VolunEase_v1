#!/usr/bin/python3
"""
Module volunteer.py

In this module volunteer data is found
"""

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Volunteer(BaseModel, Base):
    """this class contain class instnaces for this class"""
    __tablename__ = "volunteers"
    first_name = Column(String(255), nullable=False, unique=True)
    mid_name = Column(String(255), nullable=False, unique=True)
    last_name = Column(String(255), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    image = Column(String(255), nullable=True)
    phone_no = Column(String(30), nullable=False, unique=True)
    occupation = Column(String(50), nullable=False, unique=True)
    gender = Column(String(2), nullable=False, unique=True)