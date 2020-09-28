#!/usr/bin/python3
# -*- coding: utf-8 -*-

from agents.agent import Agent

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

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, pos_x: int = 0, pos_y: int = 0, dirt: int = 0):
        """Initializes pos_x, pos_y, and dirt at 0's"""
        super().__init__()
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__dirt = dirt

    def __str__(self):
        """Returns the current state of the vacuum"""
        aux_str = super().__str__() + "\n"
        aux_str += "pos_x = " + str(self.__pos_x) + "\npos_y = " + str(self.__pos_y)
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

    # _____________________________Private methods_____________________________

    # _____________________________Public methods______________________________

    def action_dirty_aspire(self) -> None:
        """This method aspires the environment."""
        self.environment.clean_square(self.__pos_x, self.__pos_y)
        print("Aspiramos la posición x: " + str(self.__pos_x) + ", y: " +
              str(self.__pos_y))

    def action_clean_move(self) -> None:
        """This method decides if the vacuum must move right or left."""
        if not self.__move_right():
            self.__move_left()

    def percept_dirt(self) -> None:
        """This method percepts if the environment is dirty"""
        self.__dirt = self.environment.is_dirty(self.__pos_x, self.__pos_y)

    def run(self, delay: int) -> None:
        """Description"""
        super().run(self.__select_action, delay)

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class VacuumError(Exception):
        def __init__(self, msg: int):
            super().__init__(msg)

    # ______________________________Inner classes______________________________


if __name__ == "__main__":
    import doctest
    doctest.testmod()