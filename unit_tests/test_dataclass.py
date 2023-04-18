"""Unit tests for the dataclass example"""
from testing_modules.dataclass import Human
import pytest


@pytest.fixture(autouse=True)
def wrap_around_test():
    """Wrap around the unit test to show examples"""
    print("before")
    yield
    print("after")


def test_alive_default() -> None:
    """Test alive default value"""
    print("test_alive_default")
    this_human = Human()
    assert this_human.alive is True


def test_height_default() -> None:
    """Test height default value"""
    print("test_height_default")
    this_human = Human()
    assert this_human.height == 5.5


def test_name_default() -> None:
    """Test name default value"""
    print("test_name_default")
    this_human = Human()
    assert this_human.name == ""


def test_name() -> None:
    """Test name assignment"""
    print("test_name")
    this_human = Human(name="bob")
    assert this_human.name == "bob"
