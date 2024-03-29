#!/usr/bin/python3
import json
import csv
import turtle
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


    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries from the JSON string representation."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Create and return an instance with all attributes set."""
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            dummy_instance = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            from models.square import Square
            dummy_instance = Square(1)
        else:
            return None
        
        dummy_instance.update(**dictionary)
        return dummy_instance
    
    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                data = cls.from_json_string(file.read())
                instances = [cls.create(**d) for d in data]
                return instances
        except FileNotFoundError:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize and save instances to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_dict().values())
    
    @classmethod
    def load_from_file_csv(cls):
        """Deserialize and load instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                data = [cls.from_csv_row(row) for row in reader]
                instances = [cls.create(**d) for d in data]
                return instances
        except FileNotFoundError:
            return []
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.width)
                turtle.left(90)

        turtle.done()

