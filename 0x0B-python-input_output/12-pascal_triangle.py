#!/usr/bin/python3
"""
Module: 12-pascal_triangle
---------------------------

This module defines a function pascal_triangle(n) that returns Pascal's triangle of n.

"""

def pascal_triangle(n):
    """
    Returns Pascal's triangle of n.

    :param n: Number of rows in Pascal's triangle.
    :type n: int
    :return: List of lists representing Pascal's triangle.
    :rtype: list of lists of integers

    Usage:
    ------
    triangle = pascal_triangle(5)
    print_triangle(triangle)

    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element in each row is always 1

        if triangle:  # For rows after the first one
            prev_row = triangle[-1]
            new_elements = [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)]
            row.extend(new_elements)

        row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle
