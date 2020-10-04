#!/usr/bin/python3
# -*- coding: utf-8 -*-

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "jun/21/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class Edge:
    """This class is a graph edge, this class supports different weights"""

    # ____________________________Class attributes_____________________________

    # ____________________________Class attributes_____________________________

    # ______________________________Class methods______________________________

    '''@classmethod
    def method_class(cls, var: dict) -> dict:
        """Method description  (DocString)"""
        return Edge.var + var'''

    # ______________________________Class methods______________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, destiny, next_edge, weights: tuple = ()):
        """Method description  (DocString)"""
        self.__weights = weights or (1, )
        self.__destiny = destiny
        self.__next = next_edge

    '''def __len__(self):
        """Method description  (DocString)
        return len(self.__string)"""
        return len(self.__string)'''

    def __str__(self):
        """Method description  (DocString)
        return object(self.__string)"""
        return " --> " + str(self.__destiny.data) + ":" + str(self.__weights)

    '''def __del__(self):
        """Method description  (DocString)
        del self.__string"""
        del self.__string'''

    # _____________________________Generic methods_____________________________

    # ____________________________Arithmetic methods___________________________

    '''def __add__(self, other):
        """Method description (DocString)"""
        return self.__weights + other.__weights

    def __sub__(self, other):
        """Method description (DocString)"""
        return self.__weights - other.__weights

    def __mul__(self, other):
        """Method description (DocString)"""
        return self.__weights * other.__weights

    def __truediv__(self, other):
        """Method description (DocString)"""
        return self.__weights / other.__weights'''

    # ____________________________Arithmetic methods___________________________

    # _____________________________Logical methods_____________________________

    '''def __lt__(self, other):
        """Method description (DocString)
        return self.__weights < other.__weights"""
        return self.__weights < other.__weights

    def __le__(self, other):
        """Method description (DocString)
        return self.__weights <= other.__weights"""
        return self.__weights <= other.__weights

    def __eq__(self, other):
        """Method description (DocString)
        return self.__weights == other.__weights"""
        return self.__weights == other.__weights'''

    # _____________________________Logical methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def weights(self) -> tuple:
        """Method description (DocString)"""
        return self.__weights

    @property
    def next(self):
        """Method description (DocString)"""
        return self.__next

    @property
    def destiny(self):
        """Method description (DocString)"""
        return self.__destiny

    # _________________________________Getters_________________________________

    # _________________________________Setters_________________________________

    '''@weights.setter
    def weights(self, weights: dict):
        """Method description (DocString)"""
        self.__weights = weights

    @next.setter
    def next(self, next: object):
        """Method description (DocString)"""
        self.__string = next'''

    # _________________________________Setters_________________________________

    # _____________________________Private methods_____________________________

    '''def __private_method(self):
        """Method description (DocString)
        >>> 2 + 3
        5
        """
        pass'''

    # _____________________________Private methods_____________________________

    # _____________________________Public methods______________________________

    '''def public_method(self):
        """Method description (DocString)
        >>> 2 + 3
        5
        """
        pass'''

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class EdgeError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________
