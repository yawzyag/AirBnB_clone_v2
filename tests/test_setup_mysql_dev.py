#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import MySQLdb


class TestDataBase(unittest.TestCase):
    """this will test the console"""
    def test_filedb(self):
        """ test database """
        # test = os.system("./setup_mysql_dev.sql")
        pass
