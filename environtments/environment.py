#!/usr/bin/python3
# -*- coding: utf-8 -*-

from agents.agent import Agent

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez, Fernanda Alvarez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "jan/01/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class Environment:
    """This is an abstract class for the real environment classes."""

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self) -> None:
        """Initializes a list of agents."""
        self.__agents = []

    def __len__(self) -> int:
        """Returns the total number of agents."""
        return self.__agents.__len__()

    def __str__(self) -> str:
        """Returns a string of agents."""
        aux_str = ""
        for i in self.__agents:
            aux_str += str(i) + "\n"
        return aux_str

    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Public methods______________________________

    def add_agent(self, agent: Agent) -> None:
        """Adds an agent in the environment list."""
        self.__agents.append(agent)

    def remove_agent(self, agent: Agent) -> None:
        """Removes an agent from the list of environment, if the agent does not
        exist it throws an error of type ValueError.
        >>> e = Environment()
        >>> e.add_agent(5)
        >>> e.add_agent(7)
        >>> print(e)
        5
        7
        <BLANKLINE>
        >>> print(e.retrieve_agent(1))
        7
        >>> e.remove_agent(5)
        """
        self.__agents.remove(agent)

    def retrieve_agent(self, index: int = 0) -> Agent:
        """Returns an agent from the list of environment, if the agent does not
        exist it throws an error of type ValueError."""
        return self.__agents[index]

    def percept(self, agent: Agent) -> None:
        """This method must be rewritten by the child class."""
        pass

    def execute_actions(self, agent: Agent) -> None:
        """This method must be rewritten by the child class."""
        pass

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class EnviromentError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________
