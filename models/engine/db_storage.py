#!/usr/bin/python3
"""Start link class to table in database"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from sqlalchemy import inspect


class DBStorage:
    """this is a class"""
    __engine = None
    __session = None

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
            s = self.__session.query(State, City, User).all()
            for sta, cit, usr in s:
                dict.update({"{}.{}".format(type(sta).__name__, sta.id): sta})
                dict.update({"{}.{}".format(type(cit).__name__, cit.id): cit})
                dict.update({"{}.{}".format(type(usr).__name__, usr.id): usr})
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
