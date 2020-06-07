#!/usr/bin/python3

"""
Unittest for Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base tests"""

    def setUp(self):
        Base._Base__nb_objects = 0