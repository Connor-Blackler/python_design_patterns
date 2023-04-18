"""A module to show the template design pattern"""
from abc import ABC, abstractmethod


class AbstractGenerator(ABC):
    """An abstract generator class"""

    def __str__(self) -> str:
        return " ".join([self._generate_1(), self._generate_2()])

    def _generate_1(self) -> str:
        return "AbstractGenerator will generate 1"

    @abstractmethod
    def _generate_2(self) -> str:
        ...


class ConcreteGenerator1(AbstractGenerator):
    """A concrete generator (1)"""

    def _generate_2(self) -> str:
        return "ConcreteGenerator1 will generate 2"


class ConcreteGenerator2(AbstractGenerator):
    """A concrete generator (2)"""

    def _generate_2(self) -> str:
        return "ConcreteGenerator2 will generate 2"

    def _generate_1(self) -> str:
        return "ConcreteGenerator2 will generate 1"


def main() -> None:
    """The main function to show the design pattern"""
    my_gen_1 = ConcreteGenerator1()
    my_gen_2 = ConcreteGenerator2()

    print(my_gen_1)
    print(my_gen_2)


main()
