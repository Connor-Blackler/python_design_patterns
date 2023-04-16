"""The main module that shows the creational design pattern"""
from dataclasses import dataclass, field
from .car_selectables.engine import *
from .car_selectables.tyre import *
from .car_selectables.radio import *
from .car_selectables.sellable import Sellable
from helpers.logger import Logger

def __compute_price(this_price: Sellable) -> float:
    return this_price.protocol_price()

@dataclass
class Car(Sellable):
    """A dataclass to emulate components of a car"""
    my_tyres: Tyres = field(default_factory=Tyres)
    my_engine: Engine = field(default_factory=BmwN63)
    my_radio: Radio = field(default_factory=SonyDsx)

    def id(self) -> str:
        return "car"

    def protocol_price(self) -> float:
        """Determine the price of the sellable object"""
        return self.my_tyres.protocol_price() + self.my_engine.protocol_price() + self.my_radio.protocol_price()

    def log(self, logger: Logger) -> None:
        """log the contents of the sellable object"""
        logger.indent()
        logger.log("tyres")
        self.my_tyres.log(logger)
        logger.unindent()

        self.my_engine.log(logger)
        self.my_radio.log(logger)

def main(log: Logger) -> None:
    """The main function to shoe the build example"""
    new_car = Car()
    new_car.my_tyres.front_left = BridgestoneSymmetric()
    new_car.my_tyres.front_right = BridgestoneDirectional()
    new_car.my_engine = BmwN63()
    new_car.my_radio = SonyDsx()

    new_car.log(log)
    log.log("total price: " + str(__compute_price(new_car)))

main(Logger())
