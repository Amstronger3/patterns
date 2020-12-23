from abc import ABC, abstractmethod


class Component(ABC):
    """
    Интерфейс Компонента объявляет метод accept, который в качестве аргумента
    может получать любой объект, реализующий интерфейс посетителя.
    """

    @abstractmethod
    def accept(self, visitor):
        pass


class Bank(Component):
    """
    Каждый Конкретный Компонент должен реализовать метод accept таким образом,
    чтобы он вызывал метод посетителя, соответствующий классу компонента.
    """

    def accept(self, visitor):
        visitor.visit_bank(self)

    def special_method_for_bank(self):
        return "Bank"


class Factory(Component):

    def accept(self, visitor):
        visitor.visit_factory(self)

    def special_method_for_factory(self):
        return "Factory"


class Court(Component):

    def accept(self, visitor):
        visitor.visit_court(self)

    def special_method_for_court(self):
        return "Court"


class Visitor(ABC):
    """
    Интерфейс Посетителя объявляет набор методов посещения, соответствующих
    классам компонентов.
    """

    @abstractmethod
    def visit_bank(self, element):
        pass

    @abstractmethod
    def visit_factory(self, element):
        pass

    @abstractmethod
    def visit_court(self, element):
        pass


class ConcreteVisitor(Visitor):

    def visit_bank(self, element):
        print(f"{element.special_method_for_bank()}")

    def visit_factory(self, element):
        print(f"{element.special_method_for_factory()}")

    def visit_court(self, element):
        print(f"{element.special_method_for_court()}")


def client_code(components, visitor):
    for component in components:
        component.accept(visitor)


components = [Bank(), Factory(), Court()]

print("Клиентский код работает с посетителем через базовый интерфейс посетителей:")
visitor = ConcreteVisitor()
client_code(components, visitor)