from abc import ABC, abstractmethod


class Captain:
    """
    Receiver - объект военного отряда
    """

    def move(self, direction):
        """
        Начать движение.
        """
        print('Судно начало движение {}'.format(direction))

    def stop(self):
        """
        Остановиться
        """
        print('Судно остановилось')


class Command(ABC):
    """
    Базовый класс для всех команд
    """

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass


class FullSpeedCommand(Command):
    """
    Команда для выполнения 'Полный вперед'
    """

    def __init__(self, stuff):
        self.stuff = stuff

    def execute(self):
        self.stuff.move('вперед')

    def unexecute(self):
        self.stuff.stop()


class ReverseCommand(Command):
    """
    Команда для движения назад
    """

    def __init__(self, stuff):
        self.stuff = stuff

    def execute(self):
        self.stuff.move('назад')

    def unexecute(self):
        self.stuff.stop()


class EngineRoomInterface:
    """
    EngineRoomInterface(Invoker) - интерфейс, через который можно отдать команды определенному отряду
    """

    def __init__(self, full_speed, reverse_command):

        self.full_speed = full_speed
        self.reverse_command = reverse_command
        self.current_command = None

    def max_speed(self):
        self.current_command = self.full_speed
        self.full_speed.execute()

    def reverse_speed(self):
        self.current_command = self.reverse_command
        self.reverse_command.execute()

    def stop(self):
        if self.current_command:
            self.current_command.unexecute()
            self.current_command = None
        else:
            print('Судно не может остановиться, так как не двигается')


stuff = Captain()
interface = EngineRoomInterface(FullSpeedCommand(stuff), ReverseCommand(stuff))
interface.max_speed()
interface.stop()
interface.reverse_speed()
interface.stop()
interface.stop()

