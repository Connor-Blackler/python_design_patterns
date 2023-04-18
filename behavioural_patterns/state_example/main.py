"""A module to show the state design pattern"""
from typing import Protocol, Callable


class StateInterface(Protocol):
    """A protocol to handle anything representing a state that can perform work"""

    def do_work(self) -> None:
        """Execute the work"""


SetStateCallback = Callable[[StateInterface], None]


class __State():
    def __init__(self, callback: SetStateCallback) -> None:
        self._callback = callback


class _stateA(__State):
    def do_work(self) -> None:
        """StateA to perform its work"""
        print("working stateA")
        print("setting to _stateB")
        self._callback(_stateB)


class _stateB(__State):
    def do_work(self) -> None:
        """StateB to perform its work"""
        print("working stateB")
        print("setting to _stateA")
        self._callback(_stateA)


class Context():
    """A class to handle the context of the state"""

    def __init__(self, initial_state: StateInterface) -> None:
        self.__set_state(initial_state)

    def __state(self) -> StateInterface:
        return self.__my_state

    def __set_state(self, _state: StateInterface) -> None:
        self.__my_state = _state(self.__set_state)

    def do_work(self) -> None:
        """the next state will perform its work"""
        self.__my_state.do_work()


def main() -> None:
    """The main function to show the state design pattern"""
    my_context = Context(_stateA)

    for i in range(1, 5):
        my_context.do_work()


main()
