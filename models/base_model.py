#!/usr/bin/pyhon3
"""
This is a Parent class that will be inherited
"""
import models
import uuid
from datetime import datetime

"""
class BaseModel that defines all common attributes/methods for other classes
"""


class BaseModel:

    def __init__(self, *args, **kwargs):
        """initializing all attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns:
        -class name
        -id and
        -attribute dictionary
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute 'updated_at'
            with the current datetime

        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of '__dict__'
            of the instance
        """
        new_dict = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
