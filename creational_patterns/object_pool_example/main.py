"""The main module that shows object pool design pattern"""
from typing import Callable
from enum import Enum
import weakref

RequestCallback = Callable[[str], None]


class Request():
    """Handles the request operation itself"""

    def request(self, request_str: str, callback: RequestCallback) -> None:
        """conduct the request itself"""
        callback("requested :" + request_str)


class RequestState(Enum):
    """Represents the state of the Request"""
    READY = 1
    INPROGRESS = 2


class RequestWrapper():
    """Wraps the request with the callback"""

    def __init__(self) -> None:
        self.__state: RequestState = RequestState.READY
        self.__my_request: Request = Request()
        self.__my_request_callable: weakref = None

    def ready(self) -> bool:
        """Determines if the request is ready to send a request"""
        return self.__state == RequestState.READY

    def __response_recieved(self, response: str) -> None:
        if self.__my_request_callable is not None:
            self.__my_request_callable(response)
        self.__state = RequestState.READY

    def request(self, request_str: str, callback: RequestCallback) -> None:
        """Send a request, calls the callback when the request has finished"""
        self.__state = RequestState.INPROGRESS
        self.__my_request_callable = weakref.proxy(callback)
        self.__my_request.request(request_str, self.__response_recieved)


class RequestPool():
    """An object pool of request objects"""

    def __init__(self) -> None:
        self.__pool: list[RequestWrapper] = list()

    def __get_request(self) -> RequestWrapper:
        for this_request in self.__pool:
            if this_request.ready():
                return this_request

        new_wrapper = RequestWrapper()
        self.__pool.append(new_wrapper)
        return new_wrapper

    def request(self, request_str: str, callback: RequestCallback):
        """
        make a new requests, assigns to an available Request if available,
        else creates a new request
        """
        self.__get_request().request(request_str, callback)


def my_callback(response: str) -> None:
    """A callback to handle the response"""
    print(response)


def main() -> None:
    """Main function to show the object pool in action"""
    __pool = RequestPool()

    __pool.request("this is my 1st request", my_callback)
    __pool.request("this is my 2nd request", my_callback)
    __pool.request("this is my 3rd request", my_callback)
    __pool.request("this is my 4th request", my_callback)
    __pool.request("this is my 5th request", my_callback)


main()
