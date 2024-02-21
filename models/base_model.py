#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, DateTime)
from os import environ


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True,
                nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            # print("*****************", kwargs, "*****************")
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs:
                del kwargs['__class__']
            # print("*****************", kwargs, "***********************")
            self.__dict__.update(kwargs)
        if environ.get("HBNB_TYPE_STORAGE") != "db":
            self.save()

    def __str__(self):
        """Returns a string representation of the instance"""
        # print("I am in the str magic method of basemodel")
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        print(str(type(self)))
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
        # return f"[{type(self).__name__}] ({self.id}) {self.to_dict()}"

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]

        # I ve added this one manually, It should be handled in the
        # line 33 above ( normally) but it does print anyway
        if "__class__" in dictionary:
            del dictionary["__class__"]
        return dictionary

    def delete(self):
        from models import storage
        """
        A method to delete the current instance from the storage
        (models.storage)
        """

        # it may need some fix, not sure
        storage.delete(self)
