#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datastructures.vertex import Vertex
from queue import PriorityQueue

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "oct/01/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class Graph:
    """This is a class of directed and non-directed graph with weights.
    In which you can change the configuration to use any weight, in the
    algorithms of the graph, such as prim kruskal, dikstra, etc."""

    # ____________________________Class attributes_____________________________

    # ____________________________Class attributes_____________________________

    # ______________________________Class methods______________________________

    '''@classmethod
    def method_class(cls, var: Vertex) -> Vertex:
        """Method description  (DocString)"""
        return Graph.var + var'''

    # ______________________________Class methods______________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, weights: tuple = (), directed: bool = True):
        """Method description  (DocString)"""
        self.__root = None
        self.__weight_index = 0
        self.__directed = directed
        self.__weights = weights

    '''def __len__(self):
        """Method description  (DocString)
        return len(self.__weight_list)"""
        return len(self.__weight_list)'''

    def __str__(self):
        """Method description  (DocString)
        return list(self.__weight_list)"""
        aux_str = "weights : " + str(self.__weights) + "\n"
        for v in self:
            aux_str += str(v) + "\n"
        return aux_str

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
        del self.__weight_list"""
        del self.__weight_list'''

    # _____________________________Generic methods_____________________________

    # ____________________________Arithmetic methods___________________________

    '''def __add__(self, other):
        """Method description (DocString)"""
        return self.__root + other.__root

    def __sub__(self, other):
        """Method description (DocString)"""
        return self.__root - other.__root

    def __mul__(self, other):
        """Method description (DocString)"""
        return self.__root * other.__root

    def __truediv__(self, other):
        """Method description (DocString)"""
        return self.__root / other.__root'''

    # ____________________________Arithmetic methods___________________________

    # _____________________________Logical methods_____________________________

    '''def __lt__(self, other):
        """Method description (DocString)
        return self.__root < other.__root"""
        return self.__root < other.__root

    def __le__(self, other):
        """Method description (DocString)
        return self.__root <= other.__root"""
        return self.__root <= other.__root

    def __eq__(self, other):
        """Method description (DocString)
        return self.__root == other.__root"""
        return self.__root == other.__root'''

    # _____________________________Logical methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    '''@property
    def root(self) -> Vertex:
        """Method description (DocString)"""
        return self.__root

    @property
    def weight_list(self) -> list:
        """Method description (DocString)"""
        return self.__weight_list'''

    # _________________________________Getters_________________________________

    # _________________________________Setters_________________________________

    '''@root.setter
    def root(self, root: Vertex):
        """Method description (DocString)"""
        self.__root = root

    @weight_list.setter
    def weight_list(self, weight_list: list):
        """Method description (DocString)"""
        self.__weight_list = weight_list'''

    # _________________________________Setters_________________________________

    # _____________________________Private methods_____________________________

    def __find_vertex(self, data: object):
        """Method description (DocString)"""
        vertex = self.__root
        while vertex:
            if vertex.data == data:
                return vertex
            vertex = vertex.next

    # _____________________________Private methods_____________________________

    # _____________________________Public methods______________________________

    def add_vertex(self, data: object):
        """Method description (DocString)"""
        self.__root = Vertex(data, self.__root)

    def add_edge(self, origin: object, destiny: object, weights: tuple = (1, )):
        """Description"""
        v_origin = self.__find_vertex(origin)
        if not v_origin:
            raise Graph.GraphError("There is no a node with these data: "
                                   + str(origin))
        v_destiny = self.__find_vertex(destiny)
        if not v_destiny:
            raise Graph.GraphError("There is no a node with these data: "
                                   + str(destiny))

        if weights.__len__() < self.__weights.__len__():
            for i in range(self.__weights.__len__() - weights.__len__()):
                weights += (1,)

        v_origin.add_edge(v_destiny, weights)
        if not self.__directed:
            v_destiny.add_edge(v_origin, weights)

    def find(self, data: object):
        """Description"""
        for v in self:
            if v.data == data:
                return v

    def bfs(self, func: "function", start: Vertex = None, *args, **kwargs):
        """Description"""
        queue = [start or self.__root]
        nodes_visited = []

        while queue:
            if queue[0] not in nodes_visited:
                nodes_visited.append(queue[0])
                func(vertex=queue[0], *args, **kwargs)

            for e in queue[0]:
                if e.destiny not in nodes_visited:
                    queue.append(e.destiny)
            del queue[0]

    def dfs(self, func: "function", start: Vertex = None, *args, **kwargs):
        """Description"""
        pile = [start or self.__root]
        nodes_visited = []

        while pile:
            if pile[-1] not in nodes_visited:
                nodes_visited.append(pile[-1])
                func(vertex=pile[-1], *args, **kwargs)
                #print(pile[-1])

            for e in pile.pop():
                if e.destiny not in nodes_visited:
                    pile.append(e.destiny)

    def dijkstra(self, start: Vertex):
        """Docstring"""
        dict_distance = {}
        dict_path = {}

        priority_queue = PriorityQueue()

        priority_queue.put((0, start.data))

        # Completa los valores iniciales de list_distance y list_path
        for vertex in self:
            dict_distance[vertex.data] = None  # asegura la convergencia
            dict_path[vertex.data] = None
        dict_distance[start.data] = 0
        #

        # Agrega los nodos a un diccionario
        graph = {}
        for vertex in self:
            aux_list = []
            for edge in vertex:
                aux_list.append((edge.weights[0], edge.destiny.data))

            graph[vertex.data] = aux_list
        #

        # Busca todas las rutas más rápidas entre nodos, tomando como base el nodo origen
        while not priority_queue.empty():
            smaller_point = priority_queue._get()
            for next_node in graph[smaller_point[1]]:  # Recorre el grafo, nodo por nodo
                if dict_distance[next_node[1]] == None or next_node[0] + dict_distance[smaller_point[1]] < \
                        dict_distance[next_node[1]]:
                    dict_distance[next_node[1]] = next_node[0] + dict_distance[smaller_point[1]]
                    dict_path[next_node[1]] = smaller_point[1]
                    priority_queue.put(next_node)

        return dict_path

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class GraphError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________
