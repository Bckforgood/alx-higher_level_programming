#!/usr/bin/python3
""" This script defines the satate object in the database
using ORM"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """This class defines the methadata for the table 'states'"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(30), nullable=False)
