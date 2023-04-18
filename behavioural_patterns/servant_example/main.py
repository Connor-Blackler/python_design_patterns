"""A module to show the servent design pattern"""
from typing import Protocol
from dataclasses import dataclass


@dataclass
class Vec2():
    """A class to emulate a 2D vector"""
    x_pos: float
    y_pos: float


class Printable(Protocol):
    """A protocol to emulate anything printable"""

    def do_print(self, location: Vec2) -> None:
        """Conducts the printing at the location"""


class Servent():
    """A servent class that handles the responsiblity of printing"""
    @staticmethod
    def print(printer_obj: Printable, location: Vec2) -> None:
        """The server will conduct the printing operation"""
        print("servant will now print, and call printer_obj.print")
        location.x_pos += 10.0
        location.y_pos += 20.0
        printer_obj.do_print(location)


class Square():
    """A class to emulate a square at a 2D positon"""

    def adjust(self, amount: Vec2) -> None:
        """Adjust the square by the amount passed"""
        Servent.print(self, amount)

    def do_print(self, location: Vec2) -> None:
        """Print the square to the location"""
        print(f"printing square at {str(location)}")


class Rectangle():
    """A class to emulate a rectangle at a 2D positon"""

    def adjust(self, amount: Vec2) -> None:
        """Adjust the rectangle by the amount passed"""
        Servent.print(self, amount)

    def do_print(self, location: Vec2) -> None:
        """Print the rectangle to the location"""
        print(f"printing rectangle at {str(location)}")


def main() -> None:
    """The main function to show the design pattern"""
    my_square = Square()
    my_rectangle = Rectangle()

    my_square.adjust(Vec2(15.0, 45.0))
    my_rectangle.adjust(Vec2(3.0, 55.0))


main()
