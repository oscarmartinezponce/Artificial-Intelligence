#!/usr/bin/python3
# -*- coding: utf-8 -*-

from environtments.environment import Environment
from agents.agent import Agent
import random

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez, Fernanda Alvarez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "sep/24/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class Floor(Environment):
    """This class represents the floor of the rooms. The Floor can be clean or
    dirty, 0 means clean, 1 means dirty"""

    # ____________________________Class attributes_____________________________

    _clean = 0
    _dirty = 1

    # ____________________________Class attributes_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, rows: int = 1, columns: int = 2):
        """Sets the number of rows, and columns, also initializes the list of
        squares cleans"""
        super(Environment, self).__init__()
        self.__squares = [[Floor._clean for i in range(columns)] for j in range(rows)]

    def __len__(self):
        """Returns the total number of rooms"""
        return len(self.__squares) * len(self.__squares[0])

    def __str__(self):
        """Returns the list of rows and columns of the rooms"""
        return str(self.__squares)

    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def rows(self) -> int:
        """Method description (DocString)"""
        return self.__squares.__len__()

    @property
    def columns(self) -> int:
        """Method description (DocString)"""
        return self.__squares[0].__len__()

    # _________________________________Getters_________________________________

    # _____________________________Private methods_____________________________

    # _____________________________Public methods______________________________

    def is_dirty(self, row: int, column: int) -> bool:
        """Returns True if the floor of the room is dirty, otherwise False, if
        the row or column does not exist it throws an exception of type
        ErrorValue"""
        return self.__squares[row][column] == Floor._dirty

    def clean_square(self, row: int, column: int) -> None:
        """Cleans the floor of a room, if the row or column does not exist it
        throws an exception of type ErrorValue"""
        self.__squares[row][column] = Floor._clean

    def dirty_square(self, row: int, column: int) -> None:
        """Dirties the floor of a room, if the row or column does not exist it
        throws an exception of type ErrorValue"""
        self.__squares[row][column] = Floor._dirty

    def dirty_squares(self) -> None:
        """Dirties the floor in random rooms"""
        self.__squares = [[random.randint(Floor._clean, Floor._dirty)
                           for i in range(self.__squares[0].__len__())]
                          for j in range(self.__squares.__len__())]

    def percept(self, agent: Agent) -> None:
        """This method reports to the agent how is the floor."""
        pass

    def execute_actions(self, agent: Agent) -> None:
        """This method must be rewritten by the child class."""
        pass

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class FloorError(Exception):
        def __init__(self, msg: int):
            super().__init__(msg)

    # ______________________________Inner classes______________________________
