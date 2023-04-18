"""A module that holds the speaking protocol, with a HouseSpeaker class"""
from typing import Protocol


class Speaker(Protocol):
    """A Protocol to emulate anything that can speak"""

    def speak(self) -> str:
        """returns the a message to speak"""


class HouseSpeaker:
    @classmethod
    def allow_speak(cls, to_speak: Speaker):
        """calls any Speaker object"""
        print(to_speak.speak())
