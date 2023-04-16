"""A module to handle all sellable tyres"""
from dataclasses import dataclass, field
from helpers.logger import Logger
from .sellable import Sellable

class Tyre(Sellable):
    """A sellable tyre"""
    def tread(self) -> str:
        """returns what type of tread does this tyre have"""
        return ""

    def id(self) -> str:
        """returns the id of the tyre"""
        return "tyre_"

class __Pirelli(Tyre):
    """An abstract baseclass for prielli tyres"""
    def protocol_price(self) -> float:
        return 150.00

    def id(self) -> str:
        return super().id() + "pirelli_" + self.tread()

class PirelliSymmetric(__Pirelli):
    """Pirelli symmetric tyres"""
    def tread(self) -> str:
        return "symmetric"

class PirelliDirectional(__Pirelli):
    """Pirelli directional tyres"""
    def tread(self) -> str:
        return "directional"

    def protocol_price(self) -> float:
        return 180.00

class __Bridgestone(Tyre):
    """An abstract baseclass for bridgestone tyres"""
    def protocol_price(self) -> float:
        return 150.00

    def id(self) -> str:
        return super().id() + "bridgestone_"  + self.tread()

class BridgestoneSymmetric(__Bridgestone):
    """Bridgestone symmetric tyres"""
    def tread(self) -> str:
        return "symmetric"

class BridgestoneDirectional(__Bridgestone):
    """Bridgestone directional tyres"""
    def protocol_price(self) -> float:
        return 160.00

    def tread(self) -> str:
        return "directional"

@dataclass
class Tyres():
    """A dataclass to hold 4 tyres"""
    front_left: Tyre = field(default_factory=PirelliDirectional)
    front_right: Tyre = field(default_factory=PirelliDirectional)
    back_left: Tyre = field(default_factory=PirelliDirectional)
    back_right: Tyre = field(default_factory=PirelliDirectional)

    def protocol_price(self) -> float:
        """The price of all four tyres"""
        return (self.front_left.protocol_price() + self.front_right.protocol_price() +
               self.back_left.protocol_price() + self.back_right.protocol_price())

    def log(self, logger: Logger) -> None:
        """Log what tyres are used"""
        self.front_left.log(logger)
        self.front_right.log(logger)
        self.back_left.log(logger)
        self.back_right.log(logger)
