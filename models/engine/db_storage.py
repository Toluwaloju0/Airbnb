#!/usr/bin/python3
""" a module to create a database storage engine """

import os

from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage():
    """ the database storage engine class """

    __engine = None
    __session = None

    def __init__(self):
        """ the initializer method for the class """



        user, pword, host, dbname = os.getenv("HBNB_MYSQL_USER"), os.getenv("HBNB_MYSQL_PWD"), os.getenv("HBNB_MYSQL_HOST"), os.getenv("HBNB_MYSQL_DB")
        
        
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{pword}@{host}/{dbname}", pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            from models.base_model import Base

            # drop all tables if the environment is test
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ a method to query the database for all instances 
        Args:
            cls (Object): the class to be queried. All classes would be queried if this is none
        """

        classes_dict = {}  # a dictionary to store the entire class which has been queried
        if cls is None:
            for cls_type in self.classes:
                for cls_instance in self.__session.scalars(select(cls_type)).all():
                    cls_dict = cls_instance.to_dict()
                    classes_dict[f"{cls_dict['__class__']}.{cls_dict['id']}"] = cls_dict
        else:
            for cls_instance in self.__session.scalars(select(cls)).all():
                cls_dict = cls_instance.to_dict()
                classes_dict[f"{cls_dict['__class__']}.{cls_dict['id']}"] = cls_dict

        return classes_dict

    def new(self, obj):
        """ a method to add an object to the database 
        Args:
            obj: the object to be added
        """

        self.__session.add(obj)

    def save(self):
        """ a method to commit all changes to the database """

        self.__session.commit()

    def delete(self, obj=None):
        """ to delete an object from the current database session
        Args:
            obj: the object to be deleted
        """

        if obj is not None:
            obj.delete()

    def reload(self):
        """ a method to create a session and the database tables"""
        
        # import all classes which inherit from Base
        from models.base_model import Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session(expire_on_commit=False)

        self.classes = [State, City, User, Place, Amenity, Review]  # a list of all the classes for a complete query
