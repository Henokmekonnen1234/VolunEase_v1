#!/usr/bin/python3
"""
Module db_storage.py
This module is ORM which interact with the database. for saving and
retriving date to or from database.
"""

from models.base_model import Base
from models.event import Event
from models.organization import Organization
from models.volunteer import Volunteer
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv

load_dotenv()

classes = {
    "Event": Event,
    "Organization": Organization,
    "Volunteer": Volunteer
}


class DBStorage:
    """This class is used to interact with database"""
    __engine = ""
    __session = ""

    def __init__(self):
        """This method will initialize the instances"""
        MYSQL_USER = getenv('MYSQL_USER')
        MYSQL_PWD = getenv('MYSQL_PWD')
        MYSQL_HOST = getenv('MYSQL_HOST')
        MYSQL_DB = getenv('MYSQL_DB')
        self.__engine = create_engine('mysql://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))
        if getenv("ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def filter(self, cls, column_name, value):
        """This will filter the values of the class"""
        value = self.__session().query(cls).filter(getattr(cls, column_name
                                                           ) == value)\
                .first()
        if value is not None:
            return value
        else:
            return None
        
    def search(self, cls, search_q, value):
        """This will filter the titles with the given letter"""
        if value == "title":
            obj = self.__session().query(cls).filter(cls.title.ilike(f'{search_q}%')).all()
            return obj
        elif value == "name":
            obj = self.__session().query(cls).filter(cls.first_name.ilike(f'{search_q}%')).all()
            if obj is not None:
                return obj
            obj = self.__session().query(cls).filter(cls.mid_name.ilike(f'{search_q}%')).all()
            if obj is not None:
                return obj
            obj = self.__session().query(cls).filter(cls.last_name.ilike(f'{search_q}%')).all()
            if obj is not None:
                return obj
        else:
            return None

    def count(self, cls=None):
        """
        count the number of objects in cls
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(self.all(clas).values())
        else:
            count = len(self.all(cls).values())

        return count