from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters


class Creator:
    """
    Создатель содержит некоторое важное состояние, которое может со временем
    меняться. Он также объявляет метод сохранения состояния внутри снимка и
    метод восстановления состояния из него.
    """

    _state = None

    def __init__(self, state):
        self._state = state
        print(f"Создатель: сейчас я на хожусь в таком состоянии: {self._state}")

    def do_something(self):
        print("Создатель: выполняю работу.")
        self._state = self._generate_random_string(30)
        print(f"Создатель: моё состояние:{self._state}")

    def _generate_random_string(self, length: int = 10):
        return "".join(sample(ascii_letters, length))

    def save(self):
        return ConcreteMemento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()
        print(f"Создатель: мое состояние поменялось на: {self._state}")


class ScreenShot(ABC):
    """
    Интерфейс Снимка предоставляет способ извлечения метаданных снимка, таких
    как дата создания или название. Однако он не раскрывает состояние Создателя.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(ScreenShot):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())

    def get_state(self):
        return self._state

    def get_name(self):
        return f"{self._date} / ({self._state})"

    def get_date(self):
        return self._date


class Conservator:
    """
    Опекун не зависит от класса Конкретного Снимка. Таким образом, он не имеет
    доступа к состоянию создателя, хранящемуся внутри снимка. Он работает со
    всеми снимками через базовый интерфейс Снимка.
    """

    def __init__(self, originator):
        self._mementos = list()
        self._originator = originator

    def backup(self):
        print("Хранитель: сохраняю текущее состояние Создателя.")
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Хранитель: откатываю состояние до: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Хранитель: здесь список скринов:")
        for memento in self._mementos:
            print(memento.get_name())


originator = Creator("Работаю работу")
caretaker = Conservator(originator)

caretaker.backup()
originator.do_something()

caretaker.backup()
originator.do_something()

caretaker.backup()
originator.do_something()

print()
caretaker.show_history()

print("Клиент: Хочу вернуть все назад!")
caretaker.undo()

print("Клиент: Еще раз вернуть все как было!")
caretaker.undo()
