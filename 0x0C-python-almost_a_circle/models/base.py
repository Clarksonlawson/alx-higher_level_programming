#!/usr/bin/python3
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
