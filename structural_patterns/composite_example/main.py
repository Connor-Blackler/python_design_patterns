"""The main module to show the composite design pattern"""
from __future__ import annotations
from helpers.logger import Logger


class Personel():
    """Emulates a person with its dependents"""

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__children: list[Personel] = []

    def name(self) -> str:
        """Returns the name of the peronsel"""
        return self.__name

    def add_personel(self, other: Personel) -> None:
        """Adds a new personel to our children"""
        self.__children.append(other)

    def report(self, log: Logger):
        """reports the structure of this personel"""
        log.indent()
        log.log(f"name: {self.__name}")
        log.indent()
        log.log("children: ")
        for this_child in self.__children:
            this_child.report(log)

        log.unindent()
        log.unindent()


class School():
    """A class to emulate a school"""

    def __init__(self, headmaster: Personel) -> None:
        self.__headmaster = headmaster

    def report(self, log: Logger):
        """reports the school heiarchy"""
        self.__headmaster.report(log)


def get_year_1() -> Personel:
    """Returns the structure of year 1"""
    child1 = Personel("child 1 from year 1")
    child2 = Personel("child 2 from year 1")
    teacher = Personel("teacher from year 1")

    teacher.add_personel(child1)
    teacher.add_personel(child2)

    return teacher


def get_year_2() -> Personel:
    """Returns the structure of year 2"""
    child1 = Personel("child 1 from year 2")
    child2 = Personel("child 2 from year 2")
    teacher = Personel("teacher from year 2")

    teacher.add_personel(child1)
    teacher.add_personel(child2)

    return teacher


def main() -> None:
    """Main function to show the composite example"""
    year_1 = get_year_1()
    year_2 = get_year_2()
    head_master = Personel("Connor Blackler")

    head_master.add_personel(year_1)
    head_master.add_personel(year_2)
    my_school = School(head_master)
    my_school.report(Logger())


main()
