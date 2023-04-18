"""A module to show the chain of responsibility design pattern"""
from __future__ import annotations
from abc import ABC, abstractmethod


class __Handler(ABC):
    """An abstract base class for handler"""
    @abstractmethod
    def set_next_handler(self, handler: __Handler) -> None:
        """Update the next handler"""

    def handle(self, request: str) -> bool:
        """handle the request"""


class __AbstractHandler(__Handler):
    """An abstract handler class"""

    def __init__(self) -> None:
        self.set_next_handler(None)

    def set_next_handler(self, handler: __Handler) -> None:
        self.__next_handler = handler

    @abstractmethod
    def handle(self, request: str) -> bool:
        if self.__next_handler:
            return self.__next_handler.handle(request)

        return False


class Bob(__AbstractHandler):
    """A class to allow Bob to handle requests"""

    def handle(self, request: str) -> bool:
        if request == "eat":
            print("Bob will now eat")
            return True
        else:
            return super().handle(request)


class Bill(__AbstractHandler):
    """A class to allow Bill to handle requests"""

    def handle(self, request: str) -> bool:
        if request == "bath":
            print("Bill will now bath")
            return True
        else:
            return super().handle(request)


class Mia(__AbstractHandler):
    """A class to allow Mia to handle requests"""

    def handle(self, request: str) -> bool:
        if request == "talk":
            print("Mia will now talk")
            return True
        else:
            return super().handle(request)


def operate(root_handler: __Handler) -> None:
    """operate, using the handler passed in"""
    actions = ["bath", "jump", "eat", "talk"]

    for this_action in actions:
        result = root_handler.handle(this_action)
        print(f"action: {this_action} handled state: {result}")


def main() -> None:
    """The main function to show the design pattern"""
    my_bob = Bob()
    my_bill = Bill()
    my_mia = Mia()

    my_bob.set_next_handler(my_bill)
    my_bill.set_next_handler(my_mia)

    operate(my_bob)


main()
