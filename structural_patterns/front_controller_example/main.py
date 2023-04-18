"""The main module to show the front controller design pattern"""
from enum import StrEnum, auto
from abc import ABC, abstractmethod


class ControlType(StrEnum):
    """An enum that emulates the different usable control types"""
    FRIDGE = auto()
    MICROWAVE = auto()
    OVEN = auto()


class _Control(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        """Abstract method to turn on the control"""

    @abstractmethod
    def _my_control_type(self) -> ControlType:
        ...

    def __eq__(self, other: ControlType) -> bool:
        return self._my_control_type() == other


class _Fridge(_Control):
    def turn_on(self) -> None:
        print("turning on the fridge")

    def _my_control_type(self) -> ControlType:
        return ControlType.FRIDGE


class _Microwave(_Control):
    def turn_on(self) -> None:
        print("turning on the microwave")

    def _my_control_type(self) -> ControlType:
        return ControlType.MICROWAVE


class _Oven(_Control):
    def turn_on(self) -> None:
        print("turning on the oven")

    def _my_control_type(self) -> ControlType:
        return ControlType.OVEN


class ControlDispatcher():
    """A class that holds all the dispatchers, and controls them directly"""

    def __init__(self) -> None:
        self._dispatchables = [_Oven(), _Microwave(), _Fridge()]

    def dispatch(self, control_type) -> None:
        """Dispatch with a matching control type"""
        for control in self._dispatchables:
            if control == control_type:
                control.turn_on()


class FrontController():
    """
    The front controller that handles what items are allowed to be dispatched
    fowards to the dispatcher if authorized
    """

    def __init__(self) -> None:
        self.__my_dispatcher = ControlDispatcher()
        self.__authorized_list = []

    def __is_authorized(self, control: ControlType) -> None:
        return control in self.__authorized_list

    def authorize(self, control: ControlType) -> None:
        """Authorize the control"""
        if not control in self.__authorized_list:
            print(f"authorizing {control}")
            self.__authorized_list.append(control)

    def dispatch(self, control: ControlType) -> None:
        """Dispatch the control"""
        if self.__is_authorized(control):
            self.__my_dispatcher.dispatch(control)
        else:
            print(f"{control} is not authorized")


def main() -> None:
    """The main function that shows the front controller design pattern"""
    my_controller = FrontController()

    my_controller.dispatch(ControlType.OVEN)
    my_controller.authorize(ControlType.OVEN)
    my_controller.dispatch(ControlType.OVEN)

    my_controller.authorize(ControlType.FRIDGE)
    my_controller.dispatch(ControlType.MICROWAVE)
    my_controller.dispatch(ControlType.FRIDGE)


main()
