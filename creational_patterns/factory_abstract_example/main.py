"""The main module that shows abstract factory design pattern"""
from abc import ABC, abstractmethod
from pathlib import Path
from .picture_importers import *
from .picture_exporters import *
from .extensions import *

class ImageConverterFactory(ABC):
    """An abstract image converter factory"""
    @abstractmethod
    def get_picture_importer(self) -> PictureImporter:
        """returns a valid importer"""

    @abstractmethod
    def get_picture_exporter(self) -> PictureExporter:
        """returns a valid exporter"""

    @abstractmethod
    def _import_exentions(self) -> list[str]:
        """returns a list of valid import extensions"""

    @abstractmethod
    def _export_exentions(self) -> list[str]:
        """returns a list of valid export extensions"""

    def is_compatible_import(self, import_extenstion: str) -> bool:
        """determines if this factory is compatible for importing"""
        if import_extenstion.lower() in self._import_exentions():
            return True

    def is_compatible_export(self, export_extenstion: str) -> bool:
        """determines if this factory is compatible for export"""
        if export_extenstion.lower() in self._export_exentions():
            return True

class PNGToJPEG(ImageConverterFactory):
    """Factory aimed to import a PNG, and export as JPEG"""

    def _import_exentions(self) -> list[str]:
        return png_extensions()

    def _export_exentions(self) -> list[str]:
        return JPEG_extensions()

    def get_picture_importer(self) -> PictureImporter:
        return PictureImporterPNG

    def get_picture_exporter(self) -> PictureExporter:
        return PictureExporterJPEG

class JPEGToPNG(ImageConverterFactory):
    """Factory aimed to import a JPEG, and export as png"""

    def _import_exentions(self) -> list[str]:
        return JPEG_extensions()

    def _export_exentions(self) -> list[str]:
        return png_extensions()

    def get_picture_importer(self) -> PictureImporter:
        return PictureImporterJPEG

    def get_picture_exporter(self) -> PictureExporter:
        return PictureExporterPNG

def get_image_factory(import_type: str, export_type: str) -> ImageConverterFactory:
    """Get the correct factory to conduct the conversion"""
    factories = [PNGToJPEG(),JPEGToPNG()]
    for factory in factories:
        if factory.is_compatible_import(import_type) and factory.is_compatible_export(export_type):
            return factory

def convert_image(image_source: Path, image_destination: Path) -> bool:
    """
    a routine that loads in a picture, converts the picture to another format, and exports.
    returns a boolean on success of fail
    """

    this_factory = get_image_factory(image_source.suffix, image_destination.suffix)
    if this_factory is None:
        return False

    importer = this_factory.get_picture_importer()()
    exporter = this_factory.get_picture_exporter()()

    #import
    importer.prepare_import(image_source)
    imported_picture = importer.do_import()

    #export
    exporter.prepare_export(imported_picture,image_destination)
    return exporter.do_export()

def main() -> None:
    """Main function that shows the abstract factory"""
    result = convert_image(Path("path/to/image1.png"), Path("path/to/image2.jpeg"))
    if not result:
        print("the PNG to JPEG conversion failed")
    else:
        print("the PNG to JPEG conversion succeeded")

    result = convert_image(Path("path/to/image1.jpg"), Path("path/to/image2.png"))
    if not result:
        print("the JPEG to PNG conversion failed")
    else:
        print("the JPEG to PNG conversion succeeded")

main()
