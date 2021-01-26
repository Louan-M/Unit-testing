#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Louan Mastrogiovanni
"""

import unittest

from main import TestDbError, ConnectionDatabaseError
from main import connect_to_db
from main import get_users_list_from_db
from main import add


class TestCase(unittest.TestCase):
    """
    Test class that checks the connection to the database using Unittest module.
    """

    def test_connect_to_db(self):
        """"""
        with self.assertRaises(TestDbError):

            # verify that Exception "TestDbError" is raised.
            connect_to_db("test")

        with self.assertRaises(ConnectionDatabaseError):

            # verify that Exception "ConnectionDatabaseError" is raised.
            connect_to_db("xxx")

    def test_get_users_from_db(self):

        users = [
            {"username": "Anne", "birthday": "11/11/1982", "role": "admin"},
            {"username": "Jean", "birthday": "13/04/1976", "role": "user"},
            {"username": "Pierre", "birthday": "05/05/1967", "role": "user"},
            {"username": "Paul", "birthday": "02/04/1964", "role": "user"},
            {"username": "Jacques", "birthday": "16/15/1998", "role": "user"},
            {"username": "Marie", "birthday": "17/08/1974", "role": "user"},
            {"username": "Sylvie", "birthday": "07/04/1970", "role": "user"},
            {"username": "Michel", "birthday": "09/12/1975", "role": "user"},
            {"username": "Françoise", "birthday": "07/12/1990", "role": "user"},
            {"username": "Florent", "birthday": "15/04/1999", "role": "user"},
            {"username": "Bertrand", "birthday": "05/08/1998", "role": "user"},
            {"username": "Hélène", "birthday": "05/12/1970", "role": "user"},
            {"username": "Louis", "birthday": "09/12/1965", "role": "user"},
            {"username": "Marie", "birthday": "01/11/1991", "role": "user"},
            {"username": "Florence", "birthday": "14/09/1987", "role": "user"},
            {"username": "Frédéric", "birthday": "01/11/1985", "role": "user"},
            {"username": "Vincent", "birthday": "11/12/1987", "role": "user"},
            {"username": "Philippe", "birthday": "26/05/1972", "role": "user"},
            {"username": "Christian", "birthday": "05/12/1999", "role": "user"},
            {"username": "Louise", "birthday": "18/01/1991", "role": "user"},
        ]

    def test_add(self):
        """ "
        Test function that verifies the add() method.
        """

        for i in range(1, 200 + 1):

            for j in range(1, 200 + 1):

                for k in range(1, 200 + 1):

                    value = i + j + k
                    assert value == add(i, j, k)


if __name__ == "__main__":
    unittest.main()
