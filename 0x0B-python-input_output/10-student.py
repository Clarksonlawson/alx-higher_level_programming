#!/usr/bin/python3
"""
Module: 10-student
-------------------

This module defines a class Student that represents a student.

"""

class Student:
    """
    Class representing a student.

    Public instance attributes:
    - first_name
    - last_name
    - age

    Methods:
    - to_json()

    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        :param first_name: The first name of the student.
        :type first_name: str
        :param last_name: The last name of the student.
        :type last_name: str
        :param age: The age of the student.
        :type age: int

        Usage:
        ------
        student = Student("John", "Doe", 23)

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        :param attrs: A list of attribute names to be retrieved. If None, retrieve all attributes.
        :type attrs: list or None
        :return: A dictionary containing the specified attributes of the Student instance.
        :rtype: dict

        Usage:
        ------
        student = Student("John", "Doe", 23)
        student_dict = student.to_json(['first_name', 'age'])
        print(student_dict)

        """
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict
