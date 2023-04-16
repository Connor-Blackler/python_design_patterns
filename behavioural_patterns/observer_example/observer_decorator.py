from __future__ import annotations
from typing import Protocol
from abc import ABC, abstractmethod

class ObserverProtocol(Protocol):
    """A class to emulate any observer"""
    def update(self, subject: AbstractSubject) -> None:
        """Calls update on the protocol"""

class AbstractSubject(ABC):
    """An abstract class to represent a subject"""
    @abstractmethod
    def subscribe(self, my_observer: ObserverProtocol) -> None:
        """Called when the user subscribes"""

    @abstractmethod
    def unsubscribe(self, my_observer: ObserverProtocol) -> None:
        """Called when the user unsubscribes"""

    @abstractmethod
    def update(self) -> None:
        """Called when an update occurs"""

def Observer(cls):
    def subscribe(self, my_observer: ObserverProtocol) -> None:
        if not my_observer in self.__observers:
            self.__observers.append(my_observer)

    def unsubscribe(self, my_observer: ObserverProtocol) -> None:
        if my_observer in self.__observers:
            self.__observers.remove(my_observer)

    def update(self) -> None:
        for this_observer in self.__observers:
            this_observer.update(self)

    setattr(cls, "__observers", [])
    setattr(cls, "subscribe", subscribe)
    setattr(cls, "unsubscribe", unsubscribe)
    setattr(cls, "update", update)

    def wrapper(*args, **kwargs):
        return cls(*args, **kwargs)

    return wrapper
