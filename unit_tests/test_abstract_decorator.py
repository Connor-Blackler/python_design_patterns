import pytest
from testing_modules.abstract_decorator import Human
from testing_modules.abstract_decorator import Dog

@pytest.fixture(autouse=True)
def wrap_around_test():
    print("before")
    yield
    print("after")

def test_age_default() -> None:
    print("test_age_default")
    this_human = Human(15)
    assert this_human.age == 18

def test_dog_default() -> None:
    print("test_dog_default")
    this_dog = Dog(3)
    assert this_dog.age == 45
