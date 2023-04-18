"""A module to show the protocal design pattern"""
from .speak import HouseSpeaker
from .clients.clients import get_clients


def main() -> None:
    """The main function to show the design pattern"""
    house = HouseSpeaker()
    for this_client in get_clients():
        house.allow_speak(this_client)


main()
