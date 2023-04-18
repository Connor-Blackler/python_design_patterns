"""A module to show the mediator design pattern"""

from typing import Protocol, Callable
from abc import ABC, abstractmethod

MediatorCallable = Callable[[str], None]


class _Operate(Protocol):
    def operate(self) -> None:
        """performs the operation of this object"""

    def event_id(self) -> str:
        """returns the event id of the operation"""


class OperateWrapper():
    """Wraps the operation with a callback"""

    def __init__(self, mediator_callback: MediatorCallable, operator: _Operate) -> None:
        self.__callback = mediator_callback
        self.__operator = operator

    def event_id(self) -> str:
        """The event id of the operator"""
        return self.__operator.event_id()

    def operate(self) -> None:
        """conducts the operation and calls the callback provided in the constructor"""
        self.__operator.operate()
        self.__callback(self.event_id())


class Mediator(ABC):
    """A base class to emulate a mediator"""
    @abstractmethod
    def event_finished(self, event_id: str) -> None:
        """Triggers when the operation has finished"""


class Operators():
    """A base class to operate an action"""

    def event_id(self) -> str:
        """event id generated from the class name"""
        return self.__class__.__name__

    def operate(self) -> None:
        """perform the operation"""
        print(f"operating {self.event_id()}")


class ConcreteMediator(Mediator):
    """A class to conduct the mediation, concrete implementation"""

    def __init__(self) -> None:
        self._step_1 = OperateWrapper(
            self.event_finished, type("knife", (Operators,), {})())
        self._step_2 = OperateWrapper(
            self.event_finished, type("plate", (Operators,), {})())
        self._step_3 = OperateWrapper(
            self.event_finished, type("steak", (Operators,), {})())

    def operate(self) -> None:
        """Start the operation process"""
        self._step_1.operate()

    def event_finished(self, event_id: str) -> None:
        """A callback that triggers when an event finishes"""
        if event_id == self._step_1.event_id():
            self._step_2.operate()

        elif event_id == self._step_2.event_id():
            self._step_3.operate()

        elif event_id == self._step_3.event_id():
            print("finished step 3")

        else:
            print("event was not handled")
            raise Exception("the mediator does not handle this event_id")


def main() -> None:
    """Show the design pattern"""
    my_mediator = ConcreteMediator()
    my_mediator.operate()


main()
