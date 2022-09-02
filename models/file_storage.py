
""" A storage location """
from models.base_model import BaseModel
import json

class FileStorage:
    """ File Storage Class. """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ A method which returns all the ditctionary objects."""
        return self.__objects

    def new(self, obj):
        """ A method which appends new elements to __objects dictionary."""
        self.__objects[obj.__class__.__name__ + "." + str(obj)] = obj

    def save(self):
        """ Serializes __objects to the JSON file path __file_path."""
        #dicti = BaseModel.to_dict(self)
        object_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w+") as file:
            json.dump(object_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists) otherwise, do nothing. If the file doesn't 
        exit no exception will be raised."""
        try:
            with open(self.__file_path, "r") as file:
                dict = json.loads(file)
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass