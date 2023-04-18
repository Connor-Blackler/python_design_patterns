"""A module to show the command design pattern"""
from typing import Protocol


class Command(Protocol):
    """A protocol to emulate anything that can execute"""

    def execute(self) -> None:
        """Execute itself"""


class CommandReciever(Protocol):
    """A protocol to emulate anything that can execute a given command"""

    def execute(self, this_command: Command) -> None:
        """Execute the command"""


class CommandWrapper():
    """A class to wrap a CommandReciever, with a list of commands to perform"""

    def __init__(self, target: CommandReciever, command_list: list[Command]) -> None:
        self.__target = target
        self.__command_list = command_list

    def execute(self) -> None:
        """execute the list of commands with the command target"""
        for this_command in self.__command_list:
            self.__target.execute(this_command)


class CommandContainer():
    """A container object that holds a command, with its pre and post command if applicable"""

    def __init__(self, my_command: Command, pre_command: Command = None,
                 post_command: Command = None) -> None:
        self.__my_command = my_command
        self.__pre_command = pre_command
        self.__post_command = post_command

    def execute(self) -> None:
        """Executes the command, whilst performing its pre command first, and post command last"""
        if self.__pre_command:
            self.__pre_command.execute()

        self.__my_command.execute()

        if self.__post_command:
            self.__post_command.execute()


class Mechanic():
    """A class to represent a mechanic"""

    def execute(self, this_command: Command) -> None:
        """The Mechanic will execute a command"""
        print("the machanic is executing a command")
        this_command.execute()


class Cleaner():
    """A class to represent a cleaner"""

    def execute(self, this_command: Command) -> None:
        """The cleaner will execute a command"""
        print("the cleaner is executing a command")
        this_command.execute()


class CleanCar():
    """A class to represent the operation of cleaning a car"""

    def execute(self) -> None:
        """execute cleaning a car"""
        print("cleaning the car")


class RemoveTyre():
    """A class to represent the operation of removing a tyre"""

    def execute(self) -> None:
        """execute removing the tyre"""
        print("removing the car tyre")


class UnboltTyre():
    """A class to represent the operation of unbolting a tyre"""

    def execute(self) -> None:
        """execute unbolting the tyre"""
        print("unbolting the car tyre")


class ReplaceTyre():
    """A class to represent the operation of replacing a tyre"""

    def execute(self) -> None:
        """execute replacing the tyre"""
        print("replacing the car tyre")


class BoltTyre():
    """A class to represent the operation of bolting a tyre"""

    def execute(self) -> None:
        """execute bolting the tyre"""
        print("bolting the car tyre")


class BossCommanding():
    """A class to represent the boss assigning work"""

    def execute(self) -> None:
        """The boss commanding orders with execute"""
        print("boss is assigning work to the mechanics")


class BossCelebrating():
    """A class to represent the boss celebrating work"""

    def execute(self) -> None:
        """The boss will perform the celebration"""
        print("boss is celebrating with the mechanics")


def main() -> None:
    """The main function to demo the design pattern"""
    my_commands = [UnboltTyre(), RemoveTyre(), ReplaceTyre(), BoltTyre()]
    my_command_wrapper = CommandWrapper(Mechanic(), my_commands)

    my_command_container = CommandContainer(
        my_command_wrapper, BossCommanding(), BossCelebrating())
    my_command_container.execute()

    my_command_wrapper = CommandWrapper(Cleaner(), [CleanCar()])
    my_command_wrapper.execute()


main()
