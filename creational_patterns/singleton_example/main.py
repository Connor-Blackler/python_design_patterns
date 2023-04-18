"""
A module that shows how to use singletons with iterators
Prevent direct appends to the private list
"""

from __future__ import annotations
from typing import Self
from testing_modules.dataclass import Human
from .singleton_decorator import singleton


class HumanA(tuple[Human]):
    """An tuple of humans with additional extention"""

    def get_males(self) -> HumanA:
        """Returns a HumanA with all males in this instance"""
        males = []
        for i in self:
            if i.sex == "male":
                males.append(i)
        return HumanA(males)


@singleton
class HumanManager:
    """A manager to manage Human objects, singleton"""

    def __init__(self) -> None:
        self.__humans = []
        self.__current_iterator = 0

    @property
    def humans(self) -> HumanA:
        """return a clone of the humans on this manager, to avoid outside manipulation"""
        return HumanA(self.__humans)

    def add_human(self, new_human: Human) -> None:
        """Append a new human to this manager"""
        self.__humans.append(new_human)

    def __str__(self) -> str:
        print(str(self.__humans))

    def __iter__(self):
        self.__current_iterator = 0
        return self

    def __next__(self):
        if self.__current_iterator >= len(self.__humans):
            del self.__current_iterator
            raise StopIteration
        else:
            ret = self.__humans[self.__current_iterator]
            self.__current_iterator += 1
            return ret


def main() -> None:
    """Main function to show the singleton design pattern"""
    mgr = HumanManager()
    mgr2 = HumanManager()
    print("is mgr == mgr2: ", mgr2 is mgr)

    mgr.add_human(Human(name="Brandy", sex="female", height="4.9"))
    mgr.add_human(Human(name="Connor"))
    mgr.add_human(Human(name="Matt"))

    for i in mgr:
        print(i)

    print("testing males")
    for i in mgr.humans.get_males():
        print(i)


main()
