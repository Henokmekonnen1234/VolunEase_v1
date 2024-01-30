#!/usr/bin/python3
"""
Module db_storage.py
This module is ORM which interact with the database. for saving and
retriving date to or from database.
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
