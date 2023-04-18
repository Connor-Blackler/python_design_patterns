"""The main module that shows the adapter design pattern"""
from .adapter_core import Cleaner


class KitchenCleaner():
    """A Cleaner to clean the kitchen"""

    def protocol_clean(self) -> None:
        """Perform the clean operation"""
        print("____ clean the kitchen")


class BedroomCleaner():
    """A Cleaner to clean the bedroom"""

    def protocol_clean(self) -> None:
        """Perform the clean operation"""
        print("____ clean the bedroom")


def main() -> None:
    """Main function"""
    kitchen_cleaner = Cleaner(KitchenCleaner())
    bedroom_cleaner = Cleaner(BedroomCleaner())

    kitchen_cleaner.clean()
    bedroom_cleaner.clean()


main()
