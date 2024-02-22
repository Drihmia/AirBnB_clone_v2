#!/usr/bin/python3
"""New engine DBStorage"""


class DBStorage:
    """ Class that define data base storage"""

    __engine = None
    __session = None

    def __init__(self):
        """ intantiation method for new engine"""

        url = 'mysql+mysqldb://{}:{}@{}:3306/{}'

        from os import environ

        USER = environ.get("HBNB_MYSQL_USER")
        PASSWD = environ.get("HBNB_MYSQL_PWD")
        HOST = environ.get("HBNB_MYSQL_HOST")
        DB = environ.get("HBNB_MYSQL_DB")
        if self.__engine is None:
            from sqlalchemy import create_engine
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review

            self.__engine = create_engine(url.format(USER, PASSWD, HOST, DB),
                                          pool_pre_ping=True)
            # print(self.__engine)

            if (environ.get("HBNB_ENV") == "test"):
                from models.base_model import Base
                Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        _class_dict = {"BaseModel": BaseModel, "User": User,
                       "State": State, "City": City, "Amenity": Amenity,
                       "Place": Place, "Review": Review
                       }
        clas_dic = {}
        query = []
        if cls:
            with self.__session() as sess:
                if self.__session:
                    query = sess.query(_class_dict[cls]).all()
        else:
            with self.__session() as sess:
                for cls in _class_dict:
                    if self.__session:
                        try:
                            query.extend(sess.query(_class_dict[cls]).all())
                        except Exception as f:
                            pass

        for obj in query:
            clas_dic.update({type(obj).__name__ + "." + obj.id: obj})
        return clas_dic

    def new(self, obj):
        """add the object to the current database session"""
        if self.__session:
            # with self.__session() as session:
            # print("-----", "new   :  ", session, "-------------")
            if obj:
                self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        if self.__session:
            # with self.__session() as session:
            self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj:
            if self.__session:
                with self.__session() as session:
                    session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy)
        create the current database session (self.__session) from the engine
        """

        if self.__engine is not None:
            from sqlalchemy.orm import sessionmaker, scoped_session
            from models.base_model import Base

            Base.metadata.create_all(bind=self.__engine)
            s = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = scoped_session(s)
            # print("-----", "reload:  ", self.__session, "-------------")
