"""The main module to show the delegation design pattern"""
from typing import Protocol


class Choppable(Protocol):
    """A Protocal for an item that can be chopped"""

    def chop(self) -> None:
        ...


class _Table():
    def prepare(self) -> None:
        """Prepare the table"""
        print("preparing the table")


class _ChoppingBoard():
    def __init__(self, items_to_chop: list[Choppable]) -> None:
        self.__choppables = items_to_chop
        self.__current_iterator = 0

    def prepare(self, my_table: _Table) -> None:
        """Prepare the chopping board onto the table"""
        my_table.prepare()
        print("placing the chopping board on the table")

    def __iter__(self):
        self.__current_iterator = 0
        return self

    def __next__(self):
        if self.__current_iterator >= len(self.__choppables):
            del self.__current_iterator
            raise StopIteration
        else:
            ret = self.__choppables[self.__current_iterator]
            self.__current_iterator += 1
            return ret

    def chop(self) -> None:
        """Perform the chop"""
        for item_to_chop in self:
            item_to_chop.chop()


class _Apple():
    def chop(self) -> None:
        """Chop the apple"""
        print("chopping the apple")


class _Pear():
    def chop(self) -> None:
        """Chop the pear"""
        print("chopping the pear")


def _chop(items_to_chop: list[Choppable]) -> None:
    my_table = _Table()
    my_chopping_board = _ChoppingBoard(items_to_chop)

    my_chopping_board.prepare(my_table)
    my_chopping_board.chop()


def main() -> None:
    """The main function to show the facade design pattern"""
    items_to_chop = [_Pear(), _Apple(), _Apple(), _Pear()]
    _chop(items_to_chop)


main()
