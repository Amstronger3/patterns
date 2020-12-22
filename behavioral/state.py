from abc import ABC, abstractmethod


class ContextFile:
    """
    Контекст определяет интерфейс, представляющий интерес для клиентов. Он также
    хранит ссылку на экземпляр подкласса Состояния, который отображает текущее
    состояние Контекста.
    """

    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):

        print(f"ContextFile: перехожу в состояние {type(state).__name__}")
        self._state = state
        self._state.context = self


    def request_render(self):
        self._state.render()

    def request_publish(self):
        self._state.publish()


class StateFile(ABC):
    """
    Базовый класс Состояния объявляет методы, которые должны реализовать все
    Конкретные Состояния, а также предоставляет обратную ссылку на объект
    Контекст, связанный с Состоянием.
    """

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def publish(self):
        pass


class DraftFile(StateFile):
    def render(self):
        print("DraftFile обрабатывает запрос render.")
        print("DraftFile хочет изменить состояние контекста файла.")
        self.context.transition_to(ModerationFile())

    def publish(self):
        print("DraftFile обрабатывает запрос publish.")


class ModerationFile(StateFile):
    def render(self):
        print("ModerationFile обрабатывает запрос render.")

    def publish(self):
        print("ModerationFile обрабатывает запрос publish.")
        print("ModerationFile хочет изменить состояние контекста файла.")
        self.context.transition_to(PublishingFile())


class PublishingFile(StateFile):
    def render(self):
        print("PublishingFile обрабатывает запрос render.")

    def publish(self):
        print("PublishingFile обрабатывает запрос publish.")
        print("Файл опубликован")


context = ContextFile(DraftFile())
context.request_render()
context.request_publish()
context.request_publish()
