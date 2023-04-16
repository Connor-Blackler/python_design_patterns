"""A module to hold the sellable base class, with the price protocol"""
from abc import ABC, abstractmethod
from typing import Protocol
from helpers.logger import Logger

class Price(Protocol):
    """A Protocol to show the price of an object"""
    def protocol_price(self) -> float:
        """The price of the object"""

class Sellable(ABC):
    """A sellable abstract class"""
    @abstractmethod
    def id(self) -> str:
        """The id of the sellable object"""

    @abstractmethod
    def protocol_price(self) -> float:
        """The price of the sellable object"""

    def log(self, logger: Logger) -> None:
        """Log the sellable object"""
        logger.indent()
        logger.log(self.id() + " : " + str(self.protocol_price()))
        logger.unindent()
