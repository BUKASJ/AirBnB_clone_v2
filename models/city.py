#!/usr/bin/python3
"""Defines the City class."""

from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """City class for AirBnB project

    state_id - empty string: it will be the State.id
    name - empty string
    """

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
