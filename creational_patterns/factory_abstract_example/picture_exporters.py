"""A module contain all the picture exporters"""
from abc import ABC, abstractmethod
from pathlib import Path
from .pictures import Picture

class PictureExporter(ABC):
    """an abstract picture exporter"""

    @abstractmethod
    def prepare_export(self, picture: Picture, src: Path):
        """a abstract method that prepares the export"""

    @abstractmethod
    def do_export(self) -> bool:
        """a abstract method that conducts the export"""

class PictureExporterPNG(PictureExporter):
    """Converts a picture to a PNG"""
    def prepare_export(self, picture: Picture, src: Path):
        """a concrete method that prepares the PNG export"""
        print("Preparing to export to PNG format")

    def do_export(self) -> bool:
        """a concrete method that conducts the PNG export"""
        print("Exporting picture to PNG format")
        return True

class PictureExporterJPEG(PictureExporter):
    """Converts a picture to a JPEG"""
    def prepare_export(self, picture: Picture, src: Path):
        """a concrete method that prepares the JPEG export"""
        print("Preparing to export to JPEG format")

    def do_export(self) -> bool:
        """a concrete method that conducts the JPEG export"""
        print("Exporting picture to JPEG format")
        return True
