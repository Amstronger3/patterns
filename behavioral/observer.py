from __future__ import annotations

from abc import ABC, abstractmethod


class Publisher(ABC):
    """
    Интферфейс издателя объявляет набор методов для управлениями подписчиками.
    """

    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcretePublisher(Publisher):
    _state: int = None

    _observers = list()

    def subscribe(self, observer):
        print(f"Издатель: добавлен новый подписчик!")
        self._observers.append(observer)

    def unsubscribe(self, observer):
        print("Издатель: подписчик удален!")
        self._observers.remove(observer)

    def notify(self):
        print("Издатель: оповещаю подписчиков")
        for observer in self._observers:
            observer.update(self)


class Follower(ABC):
    """
    Интерфейс Наблюдателя объявляет метод уведомления, который издатели
    используют для оповещения своих подписчиков.
    """

    @abstractmethod
    def update(self, subject):
        pass


class ConcreteFollowerA(Follower):

    def update(self, subject):
        print("Подписчик А: отреагировал на событие")


class ConcreteFollowerB(Follower):
    def update(self, subject):
        if subject._state == 0 or subject._state >= 2:
            print("Подписчик В: отреагировал на событие")


subject = ConcretePublisher()

follower_a = ConcreteFollowerA()
subject.subscribe(follower_a)
follower_a.update(subject)

follower_b = ConcreteFollowerB()
subject.unsubscribe(follower_a)
