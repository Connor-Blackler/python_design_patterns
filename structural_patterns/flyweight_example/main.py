"""The main module to show the flyweight design pattern"""
from dataclasses import dataclass
from creational_patterns.singleton_example.singleton_decorator import singleton

@dataclass
class _HouseSpec:
    """An object that produces house specification details"""
    bathrooms: int
    bedrooms: int

@dataclass
class _House:
    """An object that represents the house address"""
    address: str

class _SharedHouseSpec():
    """A shared house spec object used by multiple addresses"""
    def __init__(self, generic_house: _HouseSpec) -> None:
        self.__generic_house = generic_house

    def report(self, unique_state: _House) -> str:
        """Report the shared house specification"""
        return f"unique state: {unique_state} - generic state: {self.__generic_house}"

    def __str__(self) -> str:
        return str(self.__generic_house)

@singleton
class _HouseManager():
    """A House holder singleton that holds various houses on the market"""
    def __init__(self) -> None:
        specs = [_HouseSpec(1,1),_HouseSpec(1,2), _HouseSpec(2,2)]
        self.__my_flyweights = {}

        for this_spec in specs:
            self.__my_flyweights[self.__get_key(this_spec.bathrooms, this_spec.bedrooms)] = \
            self.get_flyweight(this_spec.bathrooms, this_spec.bedrooms)

    def __str__(self) -> str:
        ret = ""
        for key, value in self.__my_flyweights.items():
            ret = ret + key + ":" + str(value) + " / "

        return ret

    def __get_key(self, bathrooms: int, bedrooms: int) -> str:
        return "_".join([str(bathrooms),str(bedrooms)])

    def get_flyweight(self, bathrooms: int, bedrooms: int) -> _SharedHouseSpec:
        """returns the shared house spec matching the bathroom and bedroom count"""
        key = self.__get_key(bathrooms,bedrooms)

        if key not in self.__my_flyweights:
            print(f"creating a new flyweight for {bathrooms} , {bedrooms}")
            self.__my_flyweights[key] = _SharedHouseSpec(_HouseSpec(bathrooms, bedrooms))
        else:
            print("reusing flyweight")

        return self.__my_flyweights[key]

def add_house(address: str, bathrooms: str, bedrooms: str) -> None:
    """Adds a house to the house manager"""
    this_house_spec = _HouseManager().get_flyweight(bathrooms, bedrooms)
    print(this_house_spec.report(_House(address)))

def main() -> None:
    """The main function that shows the flyweight design pattern"""
    print(_HouseManager())

    add_house("the 2nd address", 3, 1)
    add_house("the 1st address", 1, 2)
    add_house("the 3rd address", 5, 1)

    print(_HouseManager())

main()
