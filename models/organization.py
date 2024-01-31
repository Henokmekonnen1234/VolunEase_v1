#!/usr/bin/python3
"""
Module organization.py

In this module organization data is found
"""

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Organization(BaseModel, Base):
    """this class contain class instnaces for this class"""
    __tablename__ = "organizations"
    name = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    phone_no = Column(String(30), nullable=False, unique=True)
    image = Column(String(255), nullable=True)
    website = Column(String(128), nullable=False, unique=True)
    address = Column(String(255), nullable=False)
    legal_document = Column(String(255), nullable=True)
    description = Column(String(255), nullable=False, unique=True)