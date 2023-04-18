"""A module contain a logger helper class"""


class Logger():
    """A logger class that has built in indentions"""

    def __init__(self) -> None:
        self.__indention = 0

    def log(self, this_log: str) -> None:
        """add a string to the log"""
        print(self._get_indention(), this_log)

    def _get_indention(self) -> str:
        ret = ""

        for i in range(0, self._indention_amount()):
            ret = ret + "    "

        return ret

    def _indention_amount(self) -> int:
        return self.__indention

    def indent(self) -> None:
        """Adds an indention to the log stream"""
        self.__indention += 1

    def unindent(self) -> None:
        """Removes an indention from the log stream"""
        self.__indention = max(0, self.__indention - 1)
