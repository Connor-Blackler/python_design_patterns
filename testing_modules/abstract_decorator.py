"""A module to show decorators used with abstraction"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Element(ABC):
    """A class that emulates any element"""

    def __init__(self, age: int):
        """Calls the property decerator on the subclass that is inforced by abstract method"""
        self.age = age

    def __str__(self):
        return str(self.age)

    @property
    def age(self):
        """A proprty to store the age of the element"""
        return self._age

    @age.setter
    @abstractmethod
    def age(self, new_value: int) -> int:
        """
        An exception will be thrown if this abstract method is not overwritten when
        a subclass is instanticated without implementing
        """


class Human(Element):
    """A class to emulate a human"""
    @Element.age.setter
    def age(self, new_value: int) -> int:
        self._age = new_value + 3

    def __mul__(self, other: Element):
        return Human(self._age * other._age)


class Dog(Element):
    """A class to emulate a dog"""
    @Element.age.setter
    def age(self, new_value: int) -> int:
        self._age = new_value * 15

    def __mul__(self, other: Element) -> Dog:
        return Dog(self._age * other._age)


def main() -> None:
    """The main function that shows the abstract decorator"""
    a = Human(15)
    c = Human(40)
    print(a * c)

    b = Dog(1)
    print(b)


main()
