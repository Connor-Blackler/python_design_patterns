"""The main module to show the bridge design pattern"""
from typing import Protocol


class AppleOperator(Protocol):
    """The bridge between apple, and its true provider """

    def report(self) -> None:
        """report the content"""


class RedApple():
    """Concerete red apple"""

    def report(self, size: str) -> None:
        """report the contents of this red apple"""
        print(f"producing a red apple, size: {size}")


class GreenApple():
    """Concrete green apple"""

    def report(self, size: str) -> None:
        """report the contents of this green apple"""
        print(f"producing a green apple, size: {size}")


class Apple():
    """Concrete apple, wit a injected provider"""

    def __init__(self, size: str, provider: AppleOperator) -> None:
        self.__provider = provider
        self.__size = size

    def operate(self) -> None:
        """Operate the apple, report the provider"""
        self.__provider.report(self.__size)


def main() -> None:
    """Main function that tests the bridge design pattern"""
    my_red_apple = Apple("5.5", RedApple())
    my_red_apple.operate()

    my_green_apple = Apple("3.3", GreenApple())
    my_green_apple.operate()


main()
