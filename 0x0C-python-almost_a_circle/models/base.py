#!/usr/bin/python3
import json
class Base:
    """Base class for the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with an optional custom ID."""
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects
            Base.__nb_objects += 1

    def to_json_string(self):
        """Return the JSON string representation of the object."""
        return '{"id": ' + str(self.id) + '}'

    def __init__(self, id=None):
        """Initialize Base instance with an optional custom ID."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
