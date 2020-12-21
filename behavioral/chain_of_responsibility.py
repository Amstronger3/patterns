from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков.
    """

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class PasswordHandler(AbstractHandler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового класса
    обработчика.
    """

    _next_handler: PasswordHandler = None

    def set_next(self, handler):
        self._next_handler = handler
        # Возврат обработчика отсюда позволит связать обработчики простым
        # способом, вот так:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class CheckLetter(PasswordHandler):
    """
    Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
    следующему обработчику в цепочке.
    """

    name = __qualname__

    def handle(self, request):
        if request == "буквы":
            return f"CheckLetter: Пароль не прошел валидацию потому что все символы - {request}"
        else:
            return super().handle(request)


class CheckDigit(PasswordHandler):
    name = __qualname__

    def handle(self, request):
        if request == "цифры":
            return f"CheckDigit: Пароль не прошел валидацию потому что все символы - {request}"
        else:
            return super().handle(request)


class CheckSize(PasswordHandler):
    name = __qualname__

    def handle(self, request):
        if request == "все буквы в нижнем регистре":
            return f"CheckSize: Пароль не прошел валидацию потому что {request}"
        else:
            return super().handle(request)


def client_code(handler):
    for sym in ["буквы", "цифры", "все буквы в нижнем регистре"]:
        result = handler.handle(sym)
        if result:
            print(f"{result}")
        else:
            print(f"{sym} остались не обработаны обработчиком {handler.name}")


letter = CheckLetter()
digit = CheckDigit()
size = CheckSize()

# letter.set_next(letter).set_next(size)
print("Проверка цепочки цифр:")
client_code(digit)
print()
print("Проверка цепочки регистра букв:")
client_code(size)
