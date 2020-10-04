#!/usr/bin/python3
# -*- coding: utf-8 -*-

from agents.agent import Agent
from environtments.floor import Floor
from datastructures.graph import Graph

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "sep/27/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class Vacuum(Agent):
    """This class represent a vacuum cleaner in the real life that it can
    clean his environment."""

    # ____________________________Class attributes_____________________________

    # Description of _dict_vacuum_graph
    # {(State): ('action', (next_state), (weights))
    _dict_vacuum_graph = {
        ((0, 0), (Floor._clean, Floor._clean)): ('clean_nop', ((0, 0), (Floor._clean, Floor._clean)), (1, 2)),
        ((0, 0), (Floor._clean, Floor._dirty)): ('clean_right', ((0, 1), (Floor._clean, Floor._dirty)), (1, 4)),
        ((0, 0), (Floor._dirty, Floor._clean)): ('dirty_aspire', ((0, 0), (Floor._clean, Floor._clean)), (1, 6)),
        ((0, 0), (Floor._dirty, Floor._dirty)): ('dirty_aspire', ((0, 0), (Floor._clean, Floor._dirty)), (1, 8)),
        ((0, 1), (Floor._clean, Floor._clean)): ('clean_nop', ((0, 1), (Floor._clean, Floor._clean)), (1, 10)),
        ((0, 1), (Floor._clean, Floor._dirty)): ('dirty_aspire', ((0, 1), (Floor._clean, Floor._clean)), (1, 12)),
        ((0, 1), (Floor._dirty, Floor._clean)): ('clean_left', ((0, 0), (Floor._dirty, Floor._clean)), (1, 14)),
        ((0, 1), (Floor._dirty, Floor._dirty)): ('dirty_aspire', ((0, 1), (Floor._dirty, Floor._clean)), (1, 16))
    }

    # ____________________________Class attributes_____________________________

    # ______________________________Class methods______________________________

    '''@classmethod
    def method_class(cls, var: int) -> int:
        """Method description  (DocString)"""
        return Model.var + var'''

    # ______________________________Class methods______________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, pos_x: int = 0, pos_y: int = 0, dirt: int = 0):
        """Initializes pos_x, pos_y, and dirt at 0's"""
        super().__init__()
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__dirt = dirt
        self.__score = 0
        self.__movements = 0
        self.__aux_score = 0

    def __str__(self):
        """Returns the current state of the vacuum"""
        aux_str = super().__str__() + "\n"
        aux_str += "pos_x = " + str(self.__pos_x) +\
                   "\npos_y = " + str(self.__pos_y) +\
                   "\nscore = " + str(self.__score) +\
                   "\nmovements = " + str(self.__movements) +\
                   "\nperformance average = " + str(self.performance_average)
        return aux_str

    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def pos_x(self) -> int:
        """Returns the value of pos_x"""
        return self.__pos_x

    @property
    def pos_y(self) -> int:
        """Returns the value of pos_y"""
        return self.__pos_y

    @property
    def status(self) -> tuple:
        """Return a tuple with the status"""
        x = self.__pos_x
        y = self.__pos_y
        return ((x, y), tuple(self.environment.squares[0]))

    @property
    def score(self) -> int:
        """Returns the score of the vacuum"""
        return self.__score

    @property
    def performance_average(self) -> float:
        if self.__movements:
            return self.__score / self.__movements
        else:
            return 0.0

    # _________________________________Getters_________________________________

    # _________________________________Setters_________________________________

    @pos_x.setter
    def pos_x(self, pos_x: int):
        """Sets the value of pos_x"""
        self.__pos_x = pos_x

    @pos_y.setter
    def pos_y(self, pos_y: int):
        """Sets the value of pos_y"""
        self.__pos_y = pos_y

    # _________________________________Setters_________________________________

    # _____________________________Private methods_____________________________

    def __move_right(self) -> bool:
        """This method moves the vacuum to right only if that is possible,
        If that is possible it returns True, otherwise False."""
        if self.__pos_y + 1 < self.environment.columns:
            self.__pos_y += 1
            print("Nos movimos a la derecha")
            return True

    def __move_left(self) -> bool:
        """This method moves the vacuum to left only if that is possible,
        If that is possible it returns True, otherwise False."""
        if self.__pos_y > 0:
            self.__pos_y -= 1
            print("Nos movimos a la izquierda")
            return True

    def __select_action(self) -> None:
        """Description"""
        self.percept_dirt()
        if self.__dirt:
            self.get_action('dirty')(self)
        else:
            self.get_action('clean')(self)

    def __build_graph(self, target: object = (0, 0)) -> Graph:
        """Description"""
        aux_data_vertex = ((self.__pos_x, self.__pos_y),
                           (self.environment.is_dirty(0, 0),
                            self.environment.is_dirty(0, 1)))

        graph = Graph(("fuel", "time"))
        graph.add_vertex(aux_data_vertex)
        while aux_data_vertex[1] != target:
            child_data_vertex = Vacuum._dict_vacuum_graph[aux_data_vertex]
            graph.add_vertex(child_data_vertex[1])

            graph.add_edge(aux_data_vertex, child_data_vertex[1], child_data_vertex[2])
            aux_data_vertex = child_data_vertex[1]

        return graph

    # _____________________________Private methods_____________________________

    # _____________________________Public methods______________________________

    def action_clean_right(self) -> bool:
        """This method moves the vacuum to right only if that is possible,
        If that is possible it returns True, otherwise False."""
        if self.__pos_y + 1 < self.environment.columns:
            self.__pos_y += 1
            print("Nos movimos a la derecha")
            return True

    def action_clean_left(self) -> bool:
        """This method moves the vacuum to left only if that is possible,
        If that is possible it returns True, otherwise False."""
        if self.__pos_y > 0:
            self.__pos_y -= 1
            print("Nos movimos a la izquierda")
            return True

    def action_dirty_aspire(self) -> None:
        """This method aspires the environment."""
        self.environment.clean_square(self.__pos_x, self.__pos_y)
        print("Aspiramos la posición x: " + str(self.__pos_x) + ", y: " +
              str(self.__pos_y))

    def action_clean_move(self) -> None:
        """This method decides if the vacuum must move right or left."""
        if not self.__move_right():
            self.__move_left()

    def action_clean_nop(self) -> None:
        """This method does nothing"""
        pass

    def percept_dirt(self) -> None:
        """This method percepts if the environment is dirty"""
        self.__dirt = self.environment.is_dirty(self.__pos_x, self.__pos_y)

    def run(self, delay: int, target: tuple) -> None:
        """Description"""
        super().run(self.execute_actions, delay, target)

    def actions_list(self, end_status: tuple) -> list:
        """Returns the list of actions to be performed by the vacuum."""
        action_list = []
        self.__aux_score = 0
        graph = self.__build_graph()
        dijkstra_dic = graph.dijkstra(graph.find(self.status))

        if not dijkstra_dic.get(end_status):
            aux = 0 if end_status[0][1] else 1
            end_status = ((0, aux), end_status[1])

        if dijkstra_dic.get(end_status):
            while dijkstra_dic[end_status]:
                aux_status = self._dict_vacuum_graph[dijkstra_dic[end_status]]
                self.__aux_score += aux_status[2][0]
                action_list.append(super().get_action(aux_status[0]))
                end_status = dijkstra_dic[end_status]

        return action_list

    def execute_actions(self, target: tuple) -> None:
        """This method must be rewritten by the child class."""
        actions_list = self.actions_list(target)

        while actions_list:
            actions_list.pop()(self)
            self.__movements += 1

        self.__score += self.__aux_score

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class VacuumError(Exception):
        def __init__(self, msg: int):
            super().__init__(msg)

    # ______________________________Inner classes______________________________
