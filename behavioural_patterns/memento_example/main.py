"""A module to show the memento design pattern"""

from .memento_decorator import memento
from random import randint


@memento
class NumberHolder():
    """
    Holds a number, but implements the memento decorator to add functionality
    to allow the object to be saved and restored at will
    """

    def __init__(self) -> None:
        self.my_prop_1 = 100
        self.my_prop_2 = 50
        self.my_prop_3 = 22

    def randomize(self) -> None:
        """Randomize my integers"""
        self.my_prop_1 = randint(0, 100)
        self.my_prop_2 = randint(0, 100)
        self.my_prop_3 = randint(0, 100)

    def __str__(self) -> str:
        return f"my_prop_1: {self.my_prop_1} my_prop_2: {self.my_prop_2} my_prop_3: {self.my_prop_3}"


def main() -> None:
    """The main function to show the design pattern"""
    my_number_holder = NumberHolder()

    print("first stage", my_number_holder)
    my_number_holder.save()
    my_number_holder.randomize()

    print("second stage", my_number_holder)
    my_number_holder.save()
    my_number_holder.randomize()

    print("final stage", my_number_holder)
    my_number_holder.save()
    my_number_holder.randomize()
    print("final product", my_number_holder)

    my_number_holder.restore()
    print("restore last stage", my_number_holder)

    my_number_holder.restore()
    print("restore last stage", my_number_holder)

    my_number_holder.restore()
    print("restore last stage", my_number_holder)

    my_number_holder.restore()
    print("restore no stage", my_number_holder)


main()
