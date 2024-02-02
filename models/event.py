#!/usr/bin/python3
"""
Module event.py

In this module events data is found
"""

from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship

event_student = Table("event_students", Base.metadata,
                      Column("event_id", String(60),
                             ForeignKey("events.id", onupdate="CASCADE",
                                        ondelete="CASCADE"), nullable=False,
                             primary_key=True),
                      Column("volun_id", String(60),
                             ForeignKey("volunteers.id", onupdate="CASCADE",
                                         ondelete="CASCADE"), nullable=False,
                                         primary_key=True))

class Event(BaseModel, Base):
    """this class contain class instnaces for this class"""
    __tablename__ = "events"
    title = Column(String(255), nullable=False)
    place = Column(String(255), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, )
    image = Column(String(255), nullable=True)
    org_id = Column(String(60), ForeignKey("organizations.id"),
                    nullable=False)
    description = Column(String(500), nullable=False, unique=True)
    volunteers = relationship("Volunteer", secondary=event_student,
                              viewonly=False)

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)