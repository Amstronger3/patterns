from abc import ABC, abstractmethod


class Builder(ABC):
    """
    Интерфейс Строителя объявляет создающие методы для различных частей объектов
    Продуктов.
    """

    @property
    @abstractmethod
    def car(self):
        pass

    @abstractmethod
    def manual_gear_box(self):
        pass

    @abstractmethod
    def automatic_gear_box(self):
        pass

    @abstractmethod
    def climate_control(self):
        pass

    @abstractmethod
    def light_sensor(self):
        pass


class CarBuilder(Builder):
    """
    Классы Конкретного Строителя следуют интерфейсу Строителя и предоставляют
    конкретные реализации шагов построения.
    """

    def __init__(self):
        """
        Новый экземпляр строителя должен содержать пустой объект продукта,
        который используется в дальнейшей сборке.
        """

        self.reset()

    def reset(self):
        self._car = Car()

    @property
    def car(self):
        car = self._car
        self.reset()
        return car

    def manual_gear_box(self):
        self._car.add("Механическая КПП")

    def automatic_gear_box(self):
        self._car.add("Автоматическая КПП")

    def climate_control(self):
        self._car.add("Климат контроль")

    def light_sensor(self):
        self._car.add("Датчик света")


class Car:

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Доступные конфигурации: {', '.join(self.parts)}")


class Director:
    """
    Директор отвечает только за выполнение шагов построения в определённой
    последовательности. Это полезно при производстве продуктов в определённом
    порядке или особой конфигурации.
    """

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        """
        Директор работает с любым экземпляром строителя, который передаётся ему
        клиентским кодом. Таким образом, клиентский код может изменить конечный
        тип вновь собираемого продукта.
        """
        self._builder = builder

    def build_minimum_equipment(self):
        print("Стандартная комплектация")
        self.builder.manual_gear_box()

    def build_full_equipment(self):
        print("Полная комплектация")
        self.builder.automatic_gear_box()
        self.builder.light_sensor()
        self.builder.climate_control()


"""
Клиентский код создаёт объект-строитель, передаёт его директору, а затем
инициирует процесс построения. Конечный результат извлекается из объекта-
строителя.
"""

director = Director()
builder = CarBuilder()
director.builder = builder

director.build_minimum_equipment()
builder.car.list_parts()

director.build_full_equipment()
builder.car.list_parts()

print("Индивидуальная комлпектация")
builder.manual_gear_box()
builder.automatic_gear_box()
builder.car.list_parts()
