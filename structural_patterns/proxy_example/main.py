"""The main module to show the proxy design pattern"""
from typing import Protocol

class Worker(Protocol):
    """A Protocal to emulate anything that can work"""
    def work_a(self) -> str:
        """Work the a"""

    def work_b(self) -> str:
        """Work the b"""

class Concrete():
    """A Concrete class to perform that work"""
    def work_a(self) -> str:
        """Work the a"""
        return f"{self.__class__.__name__} : work_a"

    def work_b(self) -> str:
        """Work the b"""
        return f"{self.__class__.__name__} : work_b"

class ConcreteExample1(Concrete):
    """A Concrete class to perform that work differently"""
    def work_a(self) -> str:
        return "ConcreteExample1 will handle work_a differently"

class ConcreteExample2(Concrete):
    """A Concrete class to perform that work differently"""
    def work_b(self) -> str:
        return "ConcreteExample2 will handle work_b differently"

class Boss():
    """The boss who orders the different workers"""
    def __init__(self, worker: Worker) -> None:
        self.__my_worker = worker

    def do_work(self) -> None:
        """alert the workers to perform that work in the correct order"""
        print(self.__my_worker.work_a())
        print(self.__my_worker.work_b())

def main():
    """The main function that performs that proxy design pattern"""
    my_boss_1 = Boss(ConcreteExample1())
    my_boss_2 = Boss(ConcreteExample2())

    my_boss_1.do_work()
    my_boss_2.do_work()

main()
