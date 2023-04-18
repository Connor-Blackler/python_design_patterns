"""A module to show the iterator design pattern"""


class IntA:
    """A class to emulate an array of integers"""

    def __init__(self, ints: tuple = ()) -> None:
        self.__current_iterator = 0
        self.__ints = list(ints)

    @property
    def ints(self) -> tuple[int]:
        """A proprty to hold the private ints list"""
        return tuple(self.__ints)

    def append(self, new_int: int) -> None:
        """Append a new integer to the array"""
        self.__ints.append(new_int)

    def evens(self) -> tuple[int]:
        """Returns all evens in the array"""
        ret = []
        for this_int in self.__ints:
            if this_int % 2 == 0:
                ret.append(this_int)

        return tuple(ret)

    def __str__(self) -> str:
        print(str(self.__ints))

    def __iter__(self):
        self.__current_iterator = 0
        return self

    def __next__(self):
        if self.__current_iterator >= len(self.__ints):
            del self.__current_iterator
            raise StopIteration
        else:
            ret = self.__ints[self.__current_iterator]
            self.__current_iterator += 1
            return ret


def main() -> None:
    """The main function to show the iterator design pattern"""
    my_ints = IntA((10, 3, 1, 2))
    my_ints.append(20)
    my_ints.append(7)

    for this_int in my_ints:
        print(this_int)

    print(my_ints.evens())


main()
