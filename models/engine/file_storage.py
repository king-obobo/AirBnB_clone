#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel


class FileStorage:
    """
     Serializes instances to a JSON file and
     Deserializes JSON file to instances

     Attr:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary (empty), stores all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        class_obj = FileStorage.__objects
        j_obj = {obj: class_obj[obj].to_dict() for obj in class_obj.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(j_obj, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists
        Otherwise, do nothing.
        If the file doesn’t exist, no exception is raised.
        """
        try:
            with open(FileStorage.__file_path) as f:
                json_file = json.load(f)
                for o in json_file.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
