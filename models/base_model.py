#!/usr/bin/python3
""" A class BaseModel """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ A class which creates a unique ID for users and updates time when a
     new user is created. """

    def __init__(self, *args, **kwargs):
        """Initalises arguments.
        Arguments:
                args: list of arguments
                kwargs: dictionary (key & values) of the arguments
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        models.storage.new(self)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ Saves the updated time to the current time of update."""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ The return string value for the class BaseModel. """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def to_dict(self):
        """ Saves the data into a dictionary format of python object"""
        object_map = {**self.__dict__}
        for k, v in object_map.items():
            if k in ("created_at", "updated_at"):
                object_map[k] = v.isoformat()
            else:
                object_map[k] = v
        object_map["__class__"] = self.__class__.__name__
        return (object_map)
