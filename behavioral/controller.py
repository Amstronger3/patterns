from abc import ABC


class Mediator(ABC):
    """
    Интерфейс Посредника предоставляет метод, используемый компонентами для
    уведомления посредника о различных событиях. Посредник может реагировать на
    эти события и передавать исполнение другим компонентам.
    """

    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "once":
            print("Посредник среагировал на один клик и запускает следующие операции:")
            self._component1.click_double()
        elif event == "down":
            print("Посредник среагировал на прокрутку колесиком мыши вниз и запускает следующие операции:")
            self._component2.scroll_up()


class BaseComponent(ABC):
    """
    Базовый Компонент обеспечивает базовую функциональность хранения экземпляра
    посредника внутри объектов компонентов.
    """

    def __init__(self, mediator=None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator


class Click(BaseComponent):
    def click_once(self):
        print("Один клик")
        self.mediator.notify(self, "once")

    def click_double(self):
        print("Два клика")
        self.mediator.notify(self, "double")


class Scroll(BaseComponent):
    def scroll_up(self):
        print("Прокрутка вверх")
        self.mediator.notify(self, "up")

    def scroll_down(self):
        print("Прокрутка вниз")
        self.mediator.notify(self, "down")


click = Click()
scroll = Scroll()
mediator = ConcreteMediator(click, scroll)

print("Клиент нажал на кнопку мыши:")
click.click_once()

print("Клиент прокрутил колесиком мыши:")
scroll.scroll_down()
