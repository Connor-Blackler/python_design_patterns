"""A module to show the observer design pattern"""
from .observer_decorator import Observer, AbstractSubject


@Observer
class YoutubeChannel():
    """A youtube channel, that implements the observer decorator"""

    def do_work(self) -> None:
        """Conduct some work, and update all observers"""
        print("youtube_channel is doing some work")
        self.update()


class MyHuman():
    """A human class that can observe"""

    def update(self, subject: AbstractSubject) -> None:
        """called when the observer object has updated"""
        print(subject, "human got an update")


class MyBot():
    """A bot class that can observe"""

    def update(self, subject: AbstractSubject) -> None:
        """called when the observer object has updated"""
        print(subject, "bot got an update")


class MyHybrid():
    """A hybrid class that can observe"""

    def update(self, subject: AbstractSubject) -> None:
        """called when the observer object has updated"""
        print(subject, "hybrid got an update")


def main() -> None:
    """The main function to show the design pattern"""
    my_subject = YoutubeChannel()
    my_observers = [MyHuman(), MyBot(), MyHybrid()]
    for obs in my_observers:
        my_subject.subscribe(obs)

    my_subject.do_work()


main()
