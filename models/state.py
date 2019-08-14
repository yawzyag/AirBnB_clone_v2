#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """cities"""
            cities = []
            for c, val in models.storage.all().items():
                key = c.split(".")
                if key[0] == "City" and val.state_id == str(self.id):
                    cities.append(val)
            return cities
