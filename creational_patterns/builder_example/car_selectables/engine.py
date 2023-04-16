"""A module that contains all sellable engine types"""
from .sellable import Sellable

class Engine(Sellable):
    """An abstract class to show an engine"""
    def id(self) -> str:
        return "engine_"

class __Bmw(Engine):
    def protocol_price(self) -> float:
        return 9999.99

    def id(self) -> str:
        return super().id() + "bmw"

class BmwN63(__Bmw):
    """A BMW N63 engine"""
    def id(self) -> str:
        return super().id() + "n63"

class BmwS63(__Bmw):
    """A BMW S63 engine"""
    def id(self) -> str:
        return super().id() + "s63"

    def protocol_price(self) -> float:
        return 14999.99

class __Vw(Engine):
    def protocol_price(self) -> float:
        return 3999.99

    def id(self) -> str:
        return super().id() + "bmw"

class VwCr(__Vw):
    """A VW CR engine"""
    def id(self) -> str:
        return super().id() + "cr"

class VwTdi(__Vw):
    """A VW TDI engine"""
    def id(self) -> str:
        return super().id() + "tdi"

    def protocol_price(self) -> float:
        return 6499.99
