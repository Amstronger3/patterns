from abc import ABC, abstractmethod


class InterfaceStrategy:
    """
    Контекст определяет интерфейс, представляющий интерес для клиентов.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def do_some_business_logic(self):
        result = self._strategy.do_algorithm()
        return result


class Strategy(ABC):
    """
    Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых версий
    некоторого алгоритма.
    """

    @abstractmethod
    def do_algorithm(self):
        pass


class BusStrategy(Strategy):
    def __init__(self):
        print(f"Установлена стратегия BusStrategy")

    def do_algorithm(self):
        print("Едем на автобусе по маршруту!")


class TaxiStrategy(Strategy):
    def __init__(self):
        print(f"Установлена стратегия TaxiStrategy")

    def do_algorithm(self):
        print("Едем на такси по маршруту!")


class BicycleStrategy(Strategy):
    def __init__(self):
        print(f"Установлена стратегия BicycleStrategy")

    def do_algorithm(self):
        print("Едем на велосипеде по маршруту!")


context = InterfaceStrategy(BusStrategy())
context.do_some_business_logic()
context.strategy = BicycleStrategy()
context.do_some_business_logic()
context.strategy = TaxiStrategy()
context.do_some_business_logic()
