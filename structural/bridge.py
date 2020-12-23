from abc import ABC, abstractmethod


class Abstraction:
    """
    Абстракция устанавливает интерфейс для «управляющей» части двух иерархий
    классов. Она содержит ссылку на объект из иерархии Реализации и делегирует
    ему всю настоящую работу.
    """

    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return (f"Abstraction: Базовая операция:"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):

    def operation(self):
        return (f"ExtendedAbstraction: Расширенная операция:"
                f"{self.implementation.operation_implementation()}")


class RemoteControl(ABC):
    """
    Реализация устанавливает интерфейс для всех классов реализации. Он не должен
    соответствовать интерфейсу Абстракции. На практике оба интерфейса могут быть
    совершенно разными. Как правило, интерфейс Реализации предоставляет только
    примитивные операции, в то время как Абстракция определяет операции более
    высокого уровня, основанные на этих примитивах.
    """

    @abstractmethod
    def operation_implementation(self):
        pass


class RemoteControlTv(RemoteControl):
    def operation_implementation(self):
        return "RemoteControlTv: Результат действий пульта на TV."


class RemoteControlAppleTv(RemoteControl):
    def operation_implementation(self):
        return "RemoteControlTv: Результат действий пульта на AppleTV."


class RemoteControlAndroidTv(RemoteControl):
    def operation_implementation(self):
        return "RemoteControlTv: Результат действий пульта на AndroidTV."


def client_code(abstraction):

    print(abstraction.operation())


implementation = RemoteControlTv()
abstraction = Abstraction(implementation)
client_code(abstraction)
print()
implementation = RemoteControlAppleTv()
abstraction = Abstraction(implementation)
client_code(abstraction)
print()
implementation = RemoteControlAndroidTv()
abstraction = ExtendedAbstraction(implementation)
client_code(abstraction)
