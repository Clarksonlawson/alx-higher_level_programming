#!/usr/bin/python3
"""Unit tests for the Base class."""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_creation(self):
        """Test Base instance creation."""
        base_instance = Base()
        self.assertIsInstance(base_instance, Base)

if __name__ == '__main__':
    unittest.main()
