"""A module that contains all Sellable radio types"""
from .sellable import Sellable

class Radio(Sellable):
    """A sellable radio"""
    def id(self) -> str:
        return "radio_"

class __Sony(Radio):
    def protocol_price(self) -> float:
        return 499.00

    def id(self) -> str:
        return super().id() + "sony"

class SonyDsx(__Sony):
    """A sellable Sony DSX radio"""
    def id(self) -> str:
        return super().id() + "dsx"

class SonyXav(__Sony):
    """A sellable Sony Xav radio"""
    def id(self) -> str:
        return super().id() + "xav"

    def protocol_price(self) -> float:
        return 999.00

class __Kenwood(Radio):
    def protocol_price(self) -> float:
        return 299.00

    def id(self) -> str:
        return super().id() + "kenwood"

class KenwoodDmx(__Kenwood):
    """A sellable Kenwood DMX radio"""
    def id(self) -> str:
        return super().id() + "dmx"

class KenwoodBt508(__Kenwood):
    """A sellable Kenwood BT508 radio"""
    def id(self) -> str:
        return super().id() + "bt508"

    def protocol_price(self) -> float:
        return 699.00
