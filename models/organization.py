#!/usr/bin/python3
"""
Module organization.py

In this module organization data is found
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Organization(BaseModel, Base):
    """this class contain class instnaces for this class"""
    __tablename__ = "organizations"
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password  = Column(String(255), nullable=False)
    phone_no = Column(String(30), nullable=False)
    image = Column(String(255), nullable=True)
    website = Column(String(128), nullable=False)
    address = Column(String(255), nullable=False)
    legal_document = Column(String(255), nullable=True)
    description = Column(String(1000), nullable=False)
    events = relationship("Event", backref="organizations",
                          cascade="all, delete, delete-orphan")
    volunteers =  relationship("Volunteer", backref="organizations",
                               cascade="all, delete, delete-orphan")
    
    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)