#!/usr/bin/python3
"""Unit testing for the base class"""


import os
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(TestCase):
    """The Test class for the Base class in models"""

    def test_ba(self):
        """Test the starting point of creation of Base"""
        base = Base()
        base_1 = Base()
        base_89 = Base(89)
        self.assertEqual(base.id, 1)
        self.assertEqual(base_1.id, 2)
        self.assertEqual(base_89.id, 89)

    def test_to_json_string(self):
        """Test the converting of lists to dicts"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')
        self.assertEqual(type(Base.to_json_string([{'id': 12}])), str)
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        """Test that the file saves list objects to  file"""
        Base._Base__nb_objects = 0
        Square.save_to_file(None)

        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json") as file:
            self.assertEqual(file.read(), '[]')

        Square.save_to_file([])
        with open("Square.json") as file:
            self.assertEqual(file.read(), '[]')
            self.assertEqual(type(file.read()), str)

        Square.save_to_file([Square(1)])
        with open("Square.json") as file:
            self.assertEqual(file.read(),
                             '[{"id": 1, "size": 1, "x": 0, "y": 0}]')
        Base._Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))

        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')
