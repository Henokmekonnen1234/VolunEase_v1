#!/usr/bin/python3
"""
Module volunteer.py

In this module volunteer data is found
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String 


class Volunteer(BaseModel, Base):
    """this class contain class instnaces for this class"""
    __tablename__ = "volunteers"
    first_name = Column(String(255), nullable=False, unique=False)
    mid_name = Column(String(255), nullable=False, unique=False)
    last_name = Column(String(255), nullable=False, unique=False)
    email = Column(String(128), nullable=False, unique=True)
    image = Column(String(255), nullable=True, unique=False)
    phone_no = Column(String(30), nullable=False, unique=True)
    occupation = Column(String(50), nullable=False, unique=False)
    gender = Column(String(2), nullable=False, unique=False)
    org_id = Column(String(60), ForeignKey("organizations.id"),
                    nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)