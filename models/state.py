#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    name = ""
    __tablename__ = "states"
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """cities"""
        cities = []
        for c in State.cities:
            if c.state == self.id:
                cities += c
        return cities
