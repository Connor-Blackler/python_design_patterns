"""A module to hold any dog"""
from abc import ABC, abstractmethod


class __Dog(ABC):
    @abstractmethod
    def speak(self) -> str:
        """A protocol to allow the doc to speak"""


class Boxer(__Dog):
    """A object to emulate a boxer"""

    def speak(self) -> str:
        return "woof woof (boxer)"


class Pug(__Dog):
    """A object to emulate a pug"""

    def speak(self) -> str:
        return "bark bark (pug)"


def get_clients() -> list[__Dog]:
    """Returns a list of active dog clients"""
    return [Pug(), Pug(), Boxer(), Pug(), Boxer()]
