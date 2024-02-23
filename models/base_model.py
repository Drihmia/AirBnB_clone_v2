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

    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *_, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # print("*****************", kwargs, "*****************")
        else:
            if ('updated_at' in kwargs):
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f'
                                                         )
            if ('created_at' in kwargs):
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f'
                                                         )
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)
            if not self.id:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        # print("I am in the str magic method of basemodel")
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictio = self.__dict__
        return '[{}] ({}) {}'.format(cls, self.id, dictio)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        if environ.get("HBNB_TYPE_STORAGE") == "db":
            self.updated_at = datetime.utcnow()
        else:
            self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        if ('created_at' in dictionary):
            dictionary['created_at'] = self.created_at.isoformat()
        if ('updated_at' in dictionary):
            dictionary['updated_at'] = self.updated_at.isoformat()

        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]

        return dictionary

    def delete(self):
        """
        A method to delete the current instance from the storage
        (models.storage)
        """
        from models import storage

        # it may need some fix, not sure
        storage.delete(self)
