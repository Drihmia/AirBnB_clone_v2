#!/usr/bin/python3
"""New engine DBStorage"""
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from os import environ


class DBStorage:
    """ Class that define data base storage"""

    __engine = None
    __session = None

    def __init__(self):
        """ intantiation method for new engine"""

        url = 'mysql+mysqldb://{}:{}@{}/{}'
        USER = environ.get("HBNB_MYSQL_USER")
        PASSWD = environ.get("HBNB_MYSQL_PWD")
        HOST = environ.get("HBNB_MYSQL_HOST")
        DB = environ.get("HBNB_MYSQL_DB")

        self.__engine = create_engine(url.format(USER, PASSWD, HOST, DB),
                                      pool_pre_ping=True)

        if (environ.get("HBNB_ENV") == "test"):
            from models.base_model import Base
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session"""

        _class_dict = {"BaseModel": BaseModel, "User": User,
                       "State": State, "City": City, "Amenity": Amenity,
                       "Place": Place, "Review": Review
                       }
        clas_dic = {}
        query = []
        if cls:
            if self.__session:
                query = self.__session.query(_class_dict[cls]).all()
        else:
            for cls in _class_dict:
                if self.__session:
                    try:
                        _dic = _class_dict
                        query.extend(self.__session.query(_dic[cls]).all())
                    except Exception as f:
                        pass

        for obj in query:
            clas_dic.update({type(obj).__name__ + "." + obj.id: obj})
        return clas_dic

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            if self.__session:
                self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        if self.__session:
            self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj:
            if self.__session:
                self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy)
        create the current database session (self.__session) from the engine
        """

        from sqlalchemy.orm import sessionmaker, scoped_session
        from models.base_model import Base

        Base.metadata.create_all(bind=self.__engine)
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(s)()
        # print("-----", "reload:  ", self.__session, "-------------")

    def drop_all(self):
        """drop all tables from my sql database"""
        Base.metadata.drop_all(bind=self.__engine)
