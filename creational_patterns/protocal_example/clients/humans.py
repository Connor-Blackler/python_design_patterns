"""A module to hold any human"""
from abc import ABC, abstractmethod

class __Human(ABC):
    @abstractmethod
    def speak(self) -> str:
        """A protocol to allow the human to speak"""

class Bob(__Human):
    """A human: Bob"""
    def speak(self) -> str:
        return "My name is bob, how are you?"

class Jane(__Human):
    """A human: Jane"""
    def speak(self) -> str:
        return "My name is jane, how are you?"

def get_clients() -> list[__Human]:
    """Returns a list of active human clients"""
    return [Bob(), Jane(), Bob(), Bob(), Jane()]
