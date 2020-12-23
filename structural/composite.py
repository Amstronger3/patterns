from abc import ABC, abstractmethod


class Component(ABC):
    """
    Базовый класс Компонент объявляет общие операции как для простых, так и для
    сложных объектов структуры.
    """

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def operation(self):
        """
        Базовый Компонент может сам реализовать некоторое поведение по умолчанию
        или поручить это конкретным классам, объявив метод, содержащий поведение
        абстрактным.
        """

        pass


class Product(Component):
    """
    Класс Лист представляет собой конечные объекты структуры. Лист не может
    иметь вложенных компонентов.
    """

    def operation(self):
        return "Товар"


class Box(Component):
    """
    Класс Контейнер содержит сложные компоненты, которые могут иметь вложенные
    компоненты.
    """

    def __init__(self):
        self._children = list()

    def add(self, component):
        self._children.append(component)
        component.parent = self

    def remove(self, component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self):
        return True

    def operation(self):
        results = list()
        for child in self._children:
            results.append(child.operation())
        return f"Коробка({'+'.join(results)})"


def client_code(component):
    """
    Клиентский код работает со всеми компонентами через базовый интерфейс.
    """

    print(f"Результат: {component.operation()}")


def client_code2(component1, component2):
    """
    Благодаря тому, что операции управления потомками объявлены в базовом классе
    Компонента, клиентский код может работать как с простыми, так и со сложными
    компонентами, вне зависимости от их конкретных классов.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"Результат: {component1.operation()}")


simple = Product()
print("Client: Я сделал запрос на простую компоненту - товар:")
client_code(simple)
print("\n")

tree = Box()

branch1 = Box()
branch1.add(Product())
branch1.add(Product())

branch2 = Box()
branch2.add(Product())

tree.add(branch1)
tree.add(branch2)

print("Client: Сейчас я хочу просмотреть все коробки:")
client_code(tree)
print("\n")
print("Client: Мне не нужно проверять классы компонентов даже при управлении деревом:")
client_code2(tree, simple)
