#!/usr/bin/python3

"""State class and instance of base = declarative_base()"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """fuck documentation"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
