from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Абстрактная фабрика, объявляет набор методов, которые возвращают абстрактные продукты
    """

    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_suv(self):
        pass

    @abstractmethod
    def create_sports_car(self):
        pass


class FordFactory(AbstractFactory):
    """
    Фабрика, объявляет набор методов, которые возвращают конкретные продукты
    Иными словами, завод Форд может выпускать седаны, внедорожники и спорткары.
    """

    def create_sedan(self):
        return FordSedan()

    def create_suv(self):
        return FordSuv()

    def create_sports_car(self):
        return FordSportsCar()


class DodgeFactory(AbstractFactory):
    def create_sedan(self):
        return DodgeSedan()

    def create_suv(self):
        return DodgeSuv()

    def create_sports_car(self):
        return DodgeSportsCar()


class ChevroletFactory(AbstractFactory):
    def create_sedan(self):
        return ChevroletSedan()

    def create_suv(self):
        return ChevroletSuv()

    def create_sports_car(self):
        return ChevroletSportsCar()


class AbstractSedan(ABC):
    """
    Здесь описан общий интерфейс(двигатель, кузов, колеса) продукта седан,
    который выпускает семейство(завод:Форд, Додж, Шевроле).
    """

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def body(self):
        pass

    @abstractmethod
    def wheels(self):
        pass


class FordSedan(AbstractSedan):
    """
    Здесь описан общий интерфейс для продуктов завода Форд.
    """

    def engine(self):
        print("Двигатель от седана фабрики Форд")

    def body(self):
        print("Кузов от седана фабрики Форд")

    def wheels(self):
        print("Колеса от седана фабрики Форд")


class DodgeSedan(AbstractSedan):
    """
    Здесь описан общий интерфейс для продуктов завода Додж.
    """

    def engine(self):
        print("Двигатель от седана фабрики Додж")

    def body(self):
        print("Кузов от седана фабрики Додж")

    def wheels(self):
        print("Колеса от седана фабрики Додж")


class ChevroletSedan(AbstractSedan):
    """
    Здесь описан общий интерфейс для продуктов завода Шевроле.
    """

    def engine(self):
        print("Двигатель от седана фабрики Шевроле")

    def body(self):
        print("Кузов от седана фабрики Шевроле")

    def wheels(self):
        print("Колеса от седана фабрики Шевроле")


class AbstractSuv(ABC):

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def body(self):
        pass

    @abstractmethod
    def wheels(self):
        pass


class FordSuv(AbstractSuv):
    def engine(self):
        print("Двигатель от внедорожника фабрики Форд")

    def body(self):
        print("Кузов от внедорожника фабрики Форд")

    def wheels(self):
        print("Колеса от внедорожника фабрики Форд")


class DodgeSuv(AbstractSuv):
    def engine(self):
        print("Двигатель от внедорожника фабрики Додж")

    def body(self):
        print("Кузов от внедорожника фабрики Додж")

    def wheels(self):
        print("Колеса от внедорожника фабрики Додж")


class ChevroletSuv(AbstractSuv):
    def engine(self):
        print("Двигатель от внедорожника фабрики Шевроле")

    def body(self):
        print("Кузов от внедорожника фабрики Шевроле")

    def wheels(self):
        print("Колеса от внедорожника фабрики Шевроле")


class AbstractSportsCar(ABC):
    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def body(self):
        pass

    @abstractmethod
    def wheels(self):
        pass


class FordSportsCar(AbstractSuv):
    def engine(self):
        print("Двигатель от спорткара фабрики Форд")

    def body(self):
        print("Кузов от спорткара фабрики Форд")

    def wheels(self):
        print("Колеса от спорткара фабрики Форд")


class DodgeSportsCar(AbstractSuv):
    def engine(self):
        print("Двигатель от спорткара фабрики Додж")

    def body(self):
        print("Кузов от спорткара фабрики Додж")

    def wheels(self):
        print("Колеса от спорткара фабрики Додж")


class ChevroletSportsCar(AbstractSuv):
    def engine(self):
        print("Двигатель от спорткара фабрики Шевроле")

    def body(self):
        print("Кузов от спорткара фабрики Шевроле")

    def wheels(self):
        print("Колеса от спорткара фабрики Шевроле")


def client_code(factory):
    """
    Клиентский код может работать с фабриками и продуктами.
    """
    sedan_car = factory.create_sedan()
    suv_car = factory.create_suv()
    sports_car = factory.create_sports_car()

    sedan_car.body()
    suv_car.engine()
    sports_car.wheels()


client_code(FordFactory())
client_code(DodgeFactory())
client_code(ChevroletFactory())
