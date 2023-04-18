"""Testing overriding attributes for complex unit tests"""
from pytest import MonkeyPatch


class Blah():
    """A class to test"""

    def tester(self) -> str:
        """a method that returns 2 inputs"""
        bob = input("enter your name")
        bob2 = input("enter your name")
        return bob + " " + bob2


def test_blah_tester(monkeypatch: MonkeyPatch) -> None:
    """A unit test to test the blah.tester mathod which awaits user input"""
    my_test_blah = Blah()

    inputs = ["Brandy", "Connor"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    assert my_test_blah.tester() == "Brandy Connor"
