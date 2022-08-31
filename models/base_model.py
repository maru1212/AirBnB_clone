#!/usr/bin/python3
""" A class BaseModel """
import json
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """ A class which creates a unique ID for users and updates time when a new user 
    is created. """

    def __init__(self, *args, **kwargs):
        """Initalises arguments.
        Arguments:
                args: list of arguments
                kwargs: dictionary (key & values) of the arguments
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = uuid4()
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.isoformat.strptime(value, date_format)
                elif key[0] == id:
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
    
    def save(self):
        """ Saves the updated time to the current time of update."""
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """ The return string value for the class BaseModel. """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self):
        """ Saves the data into a dictionary format of python object"""
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        object_map = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or "updated_at":
                object_map[k] = str(v)
            else:
                object_map[k] = v
        object_map["__class__"] = self.__class__.__name__
        return (object_map) 
