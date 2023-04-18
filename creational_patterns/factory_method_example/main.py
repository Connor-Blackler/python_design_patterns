"""The main module that shows factory method design pattern"""
from abc import ABC, abstractmethod
from typing import Callable

ShoppingList = Callable[[None], list[str]]


class Checkout(ABC):
    """A class that holds everything related to the checkout process"""

    def __init__(self) -> None:
        self.goodies = self.get_shopping_list()

    @abstractmethod
    def get_shopping_list(self) -> ShoppingList:
        """An abstract method to retrieve the shopping list"""

    @abstractmethod
    def _tax(self) -> float:
        ...

    def __str__(self):
        return "shopping list: " + str(self.goodies()) + " Tax amount: " + str(self._tax())


class GenericShoppingList(Checkout):
    """A class that holds a generic shopping list, not tied to tax"""

    def get_shopping_list(self):
        def my_shopping_list() -> list[str]:
            return ["apples", "beer", "crisps"]

        return my_shopping_list


class CheckoutGB(GenericShoppingList):
    """Checking out with GB"""

    def _tax(self) -> float:
        return 20.0


class CheckoutUSA(GenericShoppingList):
    """Checking out with USA"""

    def _tax(self) -> float:
        return 5.0


def main() -> None:
    """The main function to demo the design pattern"""
    my_gb = CheckoutGB()
    my_usa = CheckoutUSA()

    print(my_gb)
    print(my_usa)


main()
