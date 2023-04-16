"""A module to show simple dataclasses"""
import string
import random
from dataclasses import dataclass, field

def _generator() -> str:
    """Generates a random 32byte string"""
    return "".join(random.choices(string.ascii_lowercase, k=32))

@dataclass(frozen=False)
class Human:
    """A dataclass to emulate a human"""
    name: str = ""
    height: float = 5.5
    alive: bool = True
    sex: str = "male"
    addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=_generator)
    _searcher: str = field(init=False, repr=True)

    def __post_init__(self) -> None:
        object.__setattr__(self, '_searcher', f"{self.name} {self.addresses}")

def main() -> None:
    connor = Human(name="Connor", height=4.3, addresses=["123 weavy way","532 santa road"])
    connor.name="Connor2"#This breaks when frozen=true
    print(connor)

    brandy = Human(name="Brandy", height=2.3, addresses=["1553 ddd ddd"], sex="female")
    print(brandy)

main()
