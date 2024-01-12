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

    def test_id_increment(self):
        """Test that each new instance has a unique ID."""
        base_instance_1 = Base()
        base_instance_2 = Base()
        self.assertNotEqual(base_instance_1.id, base_instance_2.id)

    def test_custom_id(self):
        """Test creation of Base instance with custom ID."""
        custom_id = 42
        base_instance = Base(custom_id)
        self.assertEqual(base_instance.id, custom_id)

if __name__ == '__main__':
    unittest.main()
