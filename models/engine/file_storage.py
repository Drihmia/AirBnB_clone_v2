#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from pathlib import Path

        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if Path(self.__file_path).is_file():
            class_dict = {"BaseModel": BaseModel, "User": User,
                          "State": State, "City": City, "Amenity": Amenity,
                          "Place": Place, "Review": Review
                          }
            # I've replaced it with mine - DRIHMIA
            # previous implimentation, when the file is present and
            # it is empty, the console raise Errors.
            with open(self.__file_path, "r", encoding="utf-8") as f:
                try:
                    red = f.read()
                except:
                    red = ""
                if red != "":
                    dicts = json.loads(red)
                    for k, v in dicts.items():
                        for key in class_dict.keys():
                            if key in k:
                                self.__objects[k] = class_dict[key](**v)
