"""A moduel that holds all the picture importers"""
from abc import ABC, abstractmethod
from pathlib import Path
from .pictures import Picture

class PictureImporter(ABC):
    """an abstract picture importer"""

    @abstractmethod
    def prepare_import(self, src: Path):
        """a abstract method that prepares the import"""

    @abstractmethod
    def do_import(self) -> Picture:
        """a abstract method that conducts the import"""

class PictureImporterPNG(PictureImporter):
    """Converts picture to a PNG"""
    def prepare_import(self, src: Path):
        """a concrete method that prepares the PNG import"""
        print("Preparing to import a PNG")

    def do_import(self) -> Picture:
        """a concrete method that conducts the PNG import"""
        print("Importing the PNG data, and converting to a picture object")

class PictureImporterJPEG(PictureImporter):
    """converts a picture to a jpeg"""
    def prepare_import(self, src: Path):
        """a concrete method that prepares the JPEG import"""
        print("Preparing to import a JPEG")

    def do_import(self) -> Picture:
        """a concrete method that conducts the JPEG import"""
        print("Importing the JPEG data, and converting to a picture object")
