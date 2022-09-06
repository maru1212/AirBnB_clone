#!/usr/bin/python3
""" A storage location """
import json
import os


class FileStorage:
    """ File Storage Class. """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ A method which returns all the ditctionary objects."""
        return self.__objects

    def new(self, obj):
        """ A method which appends new elements to __objects dictionary."""
        key = "{}.{}".format(__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file path __file_path."""
        object_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w+") as file:
            json.dump(object_dict, file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
