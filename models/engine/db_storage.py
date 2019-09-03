#!/usr/bin/python3
"""Start link class to table in database"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class DBStorage:
    """this is a class"""
    __engine = None
    __session = None
    all_classes = {User, State, City, Review, Amenity, Place}

    def __init__(self):
        """ this is the init """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, db),
            pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ this is a comment """
        dict = {}
        if cls:
            s = self.__session.query(cls).all()
            for val in s:
                dict.update({"{}.{}".format(cls.__name__, val.id): val})
        else:
            for item in self.all_classes:
                s = self.__session.query(item).all()
                for sta in s:
                    dict.update(
                        {"{}.{}".format(type(sta).__name__, sta.id): sta})
        return dict

    def new(self, obj):
        """new to database"""
        self.__session.add(obj)

    def save(self):
        """adding save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        S = scoped_session(session)
        self.__session = S()

    def close(self):
        """reload"""
        self.__session.close()
