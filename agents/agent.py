#!/usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "sep/27/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class Agent:
    """This is an abstract class for the real agents classes."""

    # ____________________________Class attributes_____________________________

    _action = 'action'  # Initial name of agent actions

    # ____________________________Class attributes_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self) -> None:
        """Adds the agent actions automatically."""
        self.__environment = None
        self.__kill_thread = 0
        self.__actions = {}
        self.__add_actions()

    def __str__(self):
        """Returns the list of agent actions."""
        return str(self.__actions)

    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def environment(self):
        """Returns the environment of this agent."""
        return self.__environment

    # _________________________________Getters_________________________________

    # _________________________________Setters_________________________________

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this agent."""
        self.__environment = environment

    # _________________________________Setters_________________________________

    # _____________________________Private methods_____________________________

    def __add_actions(self):
        """Adds the agent actions automatically."""
        for key, value in type(self).__dict__.items():
            name = key.split("_")

            if name[0] == Agent._action:
                self.__actions[name[1] + "_" + name[2]] = value

    # _____________________________Private methods_____________________________

    # _____________________________Public methods______________________________

    def get_action(self, state: str) -> object:
        """Returns the action of the state."""
        return self.__actions[state]

    def run(self, func: object, delay: int, target: tuple) -> None:
        """Description"""
        def aux_func():
            while not self.__kill_thread:
                func(target)
                sleep(delay)
            self.__kill_thread = 0

        t = Thread(target=aux_func)
        t.start()

    def exit(self) -> None:
        """Description"""
        self.__kill_thread = 1

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class AgentError(Exception):
        def __init__(self, msg: int):
            super().__init__(msg)

    # ______________________________Inner classes______________________________
