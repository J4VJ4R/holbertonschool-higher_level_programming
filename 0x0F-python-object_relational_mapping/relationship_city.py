#!/usr/bin/python3
"""
link the class with the database
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """Class City

    Super class of city where also it has a relationship
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False, unique=True)

    name = Column(String(123),
                  nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
