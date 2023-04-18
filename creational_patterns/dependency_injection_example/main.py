"""The main module that shows dependency injection design pattern"""
from typing import Callable

Sorter = Callable[[list[int]], list[int]]


class MyNumbers():
    """A class that holds a list of numbers, and can apply different sorting routines"""

    def __init__(self, numbers: list[int]) -> None:
        self.__my_numbers = numbers

    def sort(self, sorting_routine: Sorter) -> None:
        """sort these numbers using the given sorting routine"""
        self.__my_numbers = sorting_routine(self.__my_numbers)

    def __str__(self) -> str:
        return str(self.__my_numbers)


def sort_low_to_high(numbers: list[int]) -> list[int]:
    """Sort the numbers low to high"""
    numbers.sort()
    return numbers


def sort_high_to_low(numbers: list[int]) -> list[int]:
    """Sort the numbers high to low"""
    numbers.sort(reverse=True)
    return numbers


def main() -> None:
    """The main function to show the design pattern"""
    generated_numbers = [i*i for i in range(1, 10)]
    generated_numbers.extend([i+i for i in range(1, 10)])

    numbers = MyNumbers(generated_numbers)
    print("default numbers :", numbers)

    numbers.sort(sort_low_to_high)
    print("low to high numbers :", numbers)

    numbers.sort(sort_high_to_low)
    print("high to low numbers :", numbers)


main()
