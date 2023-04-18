"""A module for the adapter protocol"""
from typing import Protocol


class Clean(Protocol):
    """A protocol that implements a clean method"""

    def protocol_clean(self) -> None:
        """clean somthing"""
