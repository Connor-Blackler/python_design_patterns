"""A module that holds all the classes related to a picture"""
from typing import Self
from dataclasses import dataclass, field
import numpy as np


@dataclass
class Pixel():
    """A class to emulate a single pixel"""
    r = np.uint8
    g = np.uint8
    b = np.uint8
    a = np.uint8


class PixelA:
    """A class to hold an array of Pixel objects"""

    def __init__(self) -> None:
        self.__pixels = list[Pixel]
        self.__current_iterator = 0

    def append(self, new_pixel: Pixel) -> None:
        """Append a new pixel to the array"""
        self.__pixels.append = new_pixel

    def __iter__(self) -> Self:
        self.__current_iterator = 0
        return self

    def __next__(self) -> Pixel:
        if self.__current_iterator >= len(self.__pixels):
            raise StopIteration
        else:
            ret = self.__pixels[self.__current_iterator]
            self.__current_iterator += 1
            return ret


@dataclass
class Picture:
    """A class top emulate a picture"""
    width: int = field(init=False)
    height: int = field(init=False)
    pixel_data = PixelA
