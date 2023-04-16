"""A Module that shows the adapter design pattern"""
from .adapter_protocol import Clean

class Cleaner():
    def __init__(self, clean: Clean) -> None:
        self.__clean = clean

    def clean(self) -> None:
        """Perform that cleaning action"""
        print("about to do some cleaning")
        self.__clean.protocol_clean()
        print("finished our cleaning")
