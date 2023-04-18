"""A module to show the visitor design pattern"""
from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractElement(ABC):
    """An abstract element"""

    def __init__(self, name: str) -> None:
        self.my_name = name

    @abstractmethod
    def accept(self, visitor: AbstractVisitor) -> None:
        """Accept the visitor to be visited"""


class ElementA(AbstractElement):
    """An element that can accept a visitor (A)"""

    def accept(self, visitor: AbstractVisitor) -> None:
        visitor.visit_a(self)


class ElementB(AbstractElement):
    """An element that can accept a visitor (B)"""

    def accept(self, visitor: AbstractVisitor) -> None:
        visitor.visit_b(self)


class AbstractVisitor(ABC):
    """An abstract visitor"""
    @abstractmethod
    def visit_a(self, element: ElementA) -> None:
        """An abstract method to allow the visitor to accept elementA"""

    @abstractmethod
    def visit_b(self, element: ElementB) -> None:
        """An abstract method to allow the visitor to accept elementB"""


class ConcreteVisitor1(AbstractVisitor):
    """A concrete visitor that handles the elements"""

    def visit_a(self, element: ElementA) -> None:
        print(f"concrete_visitor_1.visit_a: {element.my_name}")

    def visit_b(self, element: ElementB) -> None:
        print(f"concrete_visitor_1.visit_b: {element.my_name}")


class ConcreteVisitor2(AbstractVisitor):
    """A concrete visitor that handles the elements"""

    def visit_a(self, element: ElementA) -> None:
        print(f"concrete_visitor_2.visit_a: {element.my_name}")

    def visit_b(self, element: ElementB) -> None:
        print(f"concrete_visitor_2.visit_b: {element.my_name}")


def visit(elements: list[AbstractElement], visitor: AbstractVisitor):
    """A function that will iterate the elements and accept the visitor on each element"""
    for this_element in elements:
        this_element.accept(visitor)


def main() -> None:
    """The main function to show the design pattern"""
    elements = [ElementA("jane"), ElementA("julia"),
                ElementB("bill"), ElementB("harry")]

    visit(elements, ConcreteVisitor1())
    visit(elements, ConcreteVisitor2())


main()
