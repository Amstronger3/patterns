class Target:
    """
    Целевой класс объявляет интерфейс, с которым может работать клиентский код.
    """

    def request(self):
        return "Класс Target: Целевое поведение по умолчанию"


class Adaptee:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом.
    """

    def specific_request(self):
        return "юиначлому оп еинедевоп еовелеЦ"


class Adapter(Target, Adaptee):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря множественному наследованию.
    """

    def request(self) -> str:
        return f"Адаптер вернул совместимый интерфейс: {self.specific_request()[::-1]}"


def client_code(target):
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """

    print(target.request())


print("Клиент: Я могу работать только с объектами Target")

target = Target()
client_code(target)
adaptee = Adaptee()

print("Клиент: у Adaptee странное поведение. "
      "Я не понимаю его")
print(f"Adaptee: {adaptee.specific_request()}")
print("Клиент: но я могу работать с Adaptee благодаря классу Adapter:")

adapter = Adapter()
client_code(adapter)
