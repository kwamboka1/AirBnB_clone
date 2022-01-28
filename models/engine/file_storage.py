#!/usr/bin/python3
"""Defines a class FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and
       deserializes JSON file to instances
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

    def reload(self):
        """deserializes the JSON file to __objects
           only if the JSON file (__file_path) exists
        """
