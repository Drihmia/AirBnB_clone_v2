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
            self.__engine = create_engine(url.format(USER, PASSWD, HOST, DB),
                                          pool_pre_ping=True)
            if (environ.get("HBNB_ENV") == "test"):
                from models.base_model import Base
                Base.metadata.__engine.drop_all()

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
        if cls:
            if cls in _class_dict:
                if DBStorage.__session:
                    return DBStorage.__session().query(_class_dict[cls])
        else:
            clas_dic = {}
            with DBStorage.__session() as sess:
                for clas in _class_dict:
                    if DBStorage.__session:
                        print("++++++++++", _class_dict[clas], type(clas))
                        quer = sess.query(State).all()
                        print("+++++++++++++++++++++", "++++++++++++++++++++")
                        print("++++++++++++++++", type(quer), quer, "++++++++")
                        clas_dic.update({clas: quer})
            return clas_dic

    def new(self, obj):
        """add the object to the current database session"""
        if DBStorage.__session:
            DBStorage.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        if DBStorage.__session:
            DBStorage.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj:
            if DBStorage.__session:
                DBStorage.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy)
        create the current database session (self.__session) from the engine
        """

        if self.__engine is not None:
            from sqlalchemy.orm import sessionmaker, scoped_session
            from models.base_model import Base
            Base.metadata.create_all(self.__engine)
            s = sessionmaker(bind=self.__engine, expire_on_commit=False)
            DBStorage.__session = scoped_session(s)
