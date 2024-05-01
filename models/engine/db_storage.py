#!/usr/bin/python3
"""Defines the DBStorage class."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DBStorage class for HBNB project."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        from models import storage
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review, Amenity]
            objects = []
            for cls in classes:
                objects += self.__session.query(cls).all()

        return {type(obj).__name__ + '.' + obj.id: obj for obj in objects}

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()


"""DBStorage Module for HBNB project."""


class DBStorage:
    """Manages database storage."""

    def __init__(self):
        """Initialize DBStorage."""
        pass

    def all(self, cls=None):
        """Query objects from database."""
        pass

    def new(self, obj):
        """Add object to database."""
        pass

    def save(self):
        """Commit changes to database."""
        pass

    def delete(self, obj=None):
        """Delete object from database."""
        pass

    def reload(self):
        """Reload objects from database."""
        pass

    def close(self):
        """Closes database storage"""
        pass
