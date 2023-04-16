"""A module to show the strategy design pattern"""
from typing import Protocol

class NumberWorker(Protocol):
    """A class to represent any object that can work with a list of ints"""
    def work(self, workable_list: list[int]) -> list[int]:
        """Perform the work on the list, and return a worked list"""

class NumberAlteration():
    """A class to alterate a list of numbers with a given worker"""
    def __init__(self, numbers: list[int], worker: NumberWorker) -> None:
        self.__numbers = numbers
        self.worker = worker

    @property
    def worker(self) -> NumberWorker:
        """The worker performing the work"""
        return self.__worker

    @worker.setter
    def worker(self, worker: NumberWorker) -> None:
        self.__worker = worker

    def execute(self) -> list[int]:
        """Execute the number alteration using the worker"""
        this_list = self.__numbers.copy()
        this_list.extend([10,15,20])

        return self.worker.work(this_list)

class LowToHigh():
    """Convert the list: low to high"""
    def work(self, workable_list: list[int]) -> list[int]:
        """perform the conversion"""
        workable_list.sort()
        return workable_list

class HighToLow():
    """Convert the list: high to low"""
    def work(self, workable_list: list[int]) -> list[int]:
        """perform the conversion"""
        workable_list.sort(reverse=True)
        return workable_list

def main() -> None:
    """The main routine to show the design pattern"""
    my_list = [3,5,1,2,8,2,4,8]
    my_alteration = NumberAlteration(my_list, LowToHigh())
    print(my_alteration.execute())

    my_alteration.worker = HighToLow()
    print(my_alteration.execute())

main()
