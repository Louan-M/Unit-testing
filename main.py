#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Louan Mastrogiovanni
"""


from typing import List, Dict


class ConnectionDatabaseError(Exception):
    """Raised when the database connection fails."""

    pass


class TestDbError(Exception):
    """Raised when a unit test tries to connect to the database."""

    pass


def connect_to_db(connection_string: str):
    """
    Function that connects to the db.

    We will not give you access to the DB yet. So mock this function if you want to test it.

    TODO: add a unit test to verify that this function raises a ConnectionDatabaseError when a different connection string than 'test' is provided.
    TODO: add a unit test to verify that this function raises a TestDbError when a different connection string than 'test' is provided.
    """

    print("connection string: ", connection_string)

    if connection_string == "test":
        raise TestDbError("ERROR: YOU FORGOT TO MOCK connect_to_db")
    else:
        raise ConnectionDatabaseError("Can't connect to the database!")


def get_users_list_from_db(connection_string: str) -> List[Dict[str, str]]:
    """
    Function that gets the list of users from the database and returns them as a list of dict.

    Each user is formatted like that: { 'username': 'jonh Doe', 'birthday': '02/12/1985', 'role': 'admin' }
    The unit test should return at least 20 users.
    The unit test should check that all the users have a username, a birthday and a role.
    """
    db = connect_to_db(connection_string)
    users = db.get_user()
    return users


def add(x: int, y: int, z: int) -> int:
    """Addition function."""

    return x + y + z
