#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user.

    Attrs:
        email (str): Email of the user
        password (str): Password of the user
        first_name (str): The first name of the user
        last_name (str): The last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
