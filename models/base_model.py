""" A class BaseModel """
import json
import time
import uuid

class BaseModel:
    """ A class which creates a unique ID for users and updates time when a new user 
    is created. """

    def __init__(self, id=None, )