# !/usr/bin/python3
# -*- coding: utf-8 -*-

from datastructures.edge import Edge

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "oct/01/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class Vertex:
    """Class description (DocString)"""

    # ____________________________Class attributes_____________________________

    # ____________________________Class attributes_____________________________

    # ______________________________Class methods______________________________

    '''@classmethod
    def method_class(cls, var: int) -> int:
        """Method description  (DocString)"""
        return Vertex.var + var'''

    # ______________________________Class methods______________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, data: object, next_vertex):
        """Method description  (DocString)"""
        self.__root = None
        self.__data = data
        self.__next = next_vertex

    '''def __len__(self):
        """Method description  (DocString)
        return len(self.__root)"""
        return len(self.__root)'''

    def __str__(self):
        """Method description  (DocString)
        return str(self.__root)"""
        aux_str = ''
        for e in self:
            aux_str += str(e)
        return str(self.__data) + aux_str

    def __iter__(self):
        """Description"""
        self.__iter = self.__root
        return self

    def __next__(self):
        """Description"""
        while self.__iter:
            aux = self.__iter
            self.__iter = self.__iter.next
            return aux
        raise StopIteration

    '''def __del__(self):
        """Method description  (DocString)
        del self.__root"""
        del self.__root'''

    # _____________________________Generic methods_____________________________

    # ____________________________Arithmetic methods___________________________

    '''def __add__(self, other):
        """Method description (DocString)"""
        return self.__next + other.__next

    def __sub__(self, other):
        """Method description (DocString)"""
        return self.__next - other.__next

    def __mul__(self, other):
        """Method description (DocString)"""
        return self.__next * other.__next

    def __truediv__(self, other):
        """Method description (DocString)"""
        return self.__next / other.__next'''

    # ____________________________Arithmetic methods___________________________

    # _____________________________Logical methods_____________________________

    '''def __lt__(self, other):
        """Method description (DocString)
        return self.__next < other.__next"""
        return self.__next < other.__next

    def __le__(self, other):
        """Method description (DocString)
        return self.__next <= other.__next"""
        return self.__next <= other.__next

    def __eq__(self, other):
        """Method description (DocString)
        return self.__next == other.__next"""
        return self.__next == other.__next'''

    # _____________________________Logical methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def data(self):
        """Method description (DocString)"""
        return self.__data

    @property
    def next(self):
        """Method description (DocString)"""
        return self.__next

    '''@property
    def root(self) -> str:
        """Method description (DocString)"""
        return self.__root'''

    # _________________________________Getters_________________________________

    # _________________________________Setters_________________________________

    '''@next.setter
    def next(self, next):
        """Method description (DocString)"""
        self.__next = next

    @root.setter
    def root(self, root: str):
        """Method description (DocString)"""
        self.__root = root'''

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

    def add_edge(self, destiny, weights: tuple = (1,)):
        """Method description (DocString)"""
        self.__root = Edge(destiny, self.__root, weights)

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class VertexError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________
