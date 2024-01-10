#!/usr/bin/python3
"""
Module: 9-student
------------------

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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        :return: A dictionary containing the attributes of the Student instance.
        :rtype: dict

        Usage:
        ------
        student = Student("John", "Doe", 23)
        student_dict = student.to_json()
        print(student_dict)

        """
        return self.__dict__
