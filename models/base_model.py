#!/usr/bin/python3
"""Defines the BaseModel class"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes:"""
    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel
        Args:
            *args: Unused
            **kwargs (dict): Key/Value pairs of attributes.
        """
        DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "update_at":
                    self.__dict__[k] = datetime.strptime(v, DATE_FORMAT)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updates update_at with the current date and time"""
        self.update_at = datetime.today()
        models.storage.new(self)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of
        the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = datetime.today()
        dict_copy["update_at"] = datetime.today()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy

    def __str__(self):
        """
        Prints str in the form [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = dict.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
