#!/bin/usr/python3
"""
Defines unittest for models/engine/file_storage.py
    Unittest classes:
        TestFileStorage_instatiation
        TestFileStorage_methods
"""
import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """ Testing istantiation of the FileStorage class."""

    def testFileStorageinstantiation(self):
        self.assertEqual(type(FileStorage()), FileStorage)
