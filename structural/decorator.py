class Component():
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """

    def operation(self):
        pass


class LogError(Component):
    """
    Конкретные Компоненты предоставляют реализации поведения по умолчанию. Может
    быть несколько вариаций этих классов.
    """

    def operation(self):
        return "LogError"


class Decorator(Component):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты.
    """

    _component = None

    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        """
        Декоратор делегирует всю работу обёрнутому компоненту.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class NotifyByEmail(Decorator):
    """
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.
    """

    def operation(self):
        return f"NotifyByEmail({self.component.operation()})"


class NotifyByMessenger(Decorator):
    """
    Декораторы могут выполнять своё поведение до или после вызова обёрнутого
    объекта.
    """

    def operation(self):
        return f"NotifyByMessenger({self.component.operation()})"


def client_code(component):
    print(f"RESULT: {component.operation()}")


simple = LogError()
print("Client: Я могу получить как простое оповещение")
client_code(simple)
print("\n")

decorator1 = NotifyByEmail(simple)
decorator2 = NotifyByMessenger(decorator1)
print("Client: Так и по email и/или в messenger")
client_code(decorator2)
