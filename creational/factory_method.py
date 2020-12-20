from abc import ABC, abstractmethod


class CreatorTransport(ABC):
    """
    Класс Создатель объявляет фабричный метод, который должен возвращать объект
    класса Продукт. Подклассы Создателя обычно предоставляют реализацию этого
    метода.
    """

    @abstractmethod
    def create_transport(self):
        pass

    def sell(self):
        product = self.create_transport()

        result = f"Creator: The same creator's code has just worked with {product.sell()}"

        return result


class CarCreator(CreatorTransport):

    def __init__(self):
        print("Создатель автомобилей запущен")

    def create_transport(self):
        return Car()


class BikeCreator(CreatorTransport):

    def __init__(self):
        print("Создатель мотоциклов запущен")

    def create_transport(self):
        return Bike()


class CreateTransport(ABC):
    """
    Интерфейс Продукта объявляет операции, которые должны выполнять все
    конкретные продукты.
    """

    @abstractmethod
    def drive(self):
        pass


class Car(CreateTransport):

    def drive(self):
        return f"автомобиль готов к поездке"


class Bike(CreateTransport):

    def drive(self):
        return f"мотоцикл готов к поездке"


def client_code(creator):
    """
    Клиентский код работает с экземпляром конкретного создателя, хотя и через
    его базовый интерфейс. Пока клиент продолжает работать с создателем через
    базовый интерфейс, вы можете передать ему любой подкласс создателя.
    """
    transport = creator.create_transport()
    print(f"Клиент: Я не знаю класс создателя и все же "
          f"{transport.drive()}")


client_code(CarCreator())
client_code(BikeCreator())
