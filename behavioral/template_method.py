from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    Абстрактный Класс определяет шаблонный метод, содержащий скелет некоторого
    алгоритма, состоящего из вызовов (обычно) абстрактных примитивных операций.

    Конкретные подклассы должны реализовать эти операции, но оставить сам
    шаблонный метод без изменений.
    """

    def template_method(self):
        """
        Шаблонный метод определяет скелет алгоритма.
        """

        self.mine()
        self.open_file()
        self.extract_data()
        self.parse_data()
        self.analyze_data()
        self.send_report()
        self.close_file()

    def open_file(self):
        print("AbstractClass: Я могу открыть файл своим методом open_file")

    def parse_data(self):
        print("AbstractClass: Я могу прочитать данные файла своим методом parse_data")

    def close_file(self):
        print("AbstractClass: Я могу закрыть файл своим методом close_data")

    @abstractmethod
    def extract_data(self):
        pass

    @abstractmethod
    def analyze_data(self):
        pass

    def send_report(self):
        pass

    def mine(self):
        pass


class FilePDF(AbstractClass):
    """
    Конкретные классы должны реализовать все абстрактные операции базового
    класса. Они также могут переопределить некоторые операции с реализацией по
    умолчанию.
    """

    def extract_data(self):
        print("FilePDF: Извлекаю данные из файла")

    def analyze_data(self):
        print("FilePDF: Анализирую данные из файла")


class FileDoc(AbstractClass):

    def extract_data(self):
        print("FileDoc: Извлекаю данные из файла")

    def analyze_data(self):
        print("FileDoc: Анализирую данные из файла")

    def send_report(self):
        print("FileDoc: Отправляю отчет (как опция)")


def client_code(abstract_class):
    abstract_class.template_method()


client_code(FileDoc())
