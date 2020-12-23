class Facade:
    """
    Класс Фасада предоставляет простой интерфейс для сложной логики одной или
    нескольких подсистем. Фасад делегирует запросы клиентов соответствующим
    объектам внутри подсистемы. Фасад также отвечает за управление их жизненным
    циклом. Все это защищает клиента от нежелательной сложности подсистемы.
    """

    def __init__(self, subsystem1, subsystem2):

        self._subsystem1 = subsystem1 or ConvertVideo()
        self._subsystem2 = subsystem2 or ConvertAudio()

    def operation(self):

        results = list()
        results.append("Фасад инициализирует такие подсистемы:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class ConvertVideo:
    """
    Подсистема может принимать запросы либо от фасада, либо от клиента напрямую.
    В любом случае, для Подсистемы Фасад – это ещё один клиент, и он не является
    частью Подсистемы.
    """

    def operation1(self):
        return "ConvertVideo: Подготовка к конвертации видео."

    def operation_n(self):
        return "ConvertVideo: Конвертирую видео!"


class ConvertAudio:

    def operation1(self) -> str:
        return "ConvertAudio: Подготовка к конвертации аудио."

    def operation_z(self) -> str:
        return "ConvertAudio: Конвертирую аудио!"


def client_code(facade):
    """
    Клиентский код работает со сложными подсистемами через простой интерфейс,
    предоставляемый Фасадом. Когда фасад управляет жизненным циклом подсистемы,
    клиент может даже не знать о существовании подсистемы. Такой подход
    позволяет держать сложность под контролем.
    """

    print(facade.operation())


subsystem1 = ConvertVideo()
subsystem2 = ConvertAudio()
facade = Facade(subsystem1, subsystem2)
client_code(facade)
