"""The main module to show the delegation design pattern"""
from abc import ABC, abstractmethod


class Fruit(ABC):
    """An abstract class to emulate a fruit"""
    @abstractmethod
    def slice(self):
        """Abstract method to slice the fruit"""


class Orange(Fruit):
    """A concrete class for an Orange"""

    def slice(self):
        print("slicing the orange")


class Apple(Fruit):
    """A concrete class for an Apple"""

    def slice(self):
        print("slicing the apple")


class FruitBowl():
    """A class to emulate a fruitbowl"""

    def __init__(self) -> None:
        self.__fruit = [Orange(), Apple(), Apple(), Orange(), Apple()]

    def slice_oranges(self) -> None:
        """Slice all the oranges in this fruitbowl"""
        for this_fruit in self.__fruit:
            if isinstance(this_fruit, Orange):
                this_fruit.slice()


class Table():
    """A class to emulate a table"""

    def __init__(self) -> None:
        self._fruit_bowl = FruitBowl()
        self.__fruit_bowl_methods = [f for f in dir(
            FruitBowl) if not f.startswith('_')]

    def __getattr__(self, func):
        """Delegate calls to the fruit bowl if the fruitbowl has the method"""
        def method(*args, **kwargs):
            if func in self.__fruit_bowl_methods:
                return getattr(self._fruit_bowl, func)(*args, **kwargs)
            else:
                raise AttributeError

        return method


def main() -> None:
    """The main function that shows the delegation design pattern"""
    my_table = Table()
    my_table.slice_oranges()


main()
