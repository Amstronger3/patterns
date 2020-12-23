from collections.abc import Iterable, Iterator


class ConcreteIterator(Iterator):
    """
    Конкретные Итераторы реализуют различные алгоритмы обхода. Эти классы
    постоянно хранят текущее положение обхода.
    """

    _position: int = None

    _reverse: bool = False

    def __init__(self, collection, reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):

        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class Collection(Iterable):
    """
    Конкретные Коллекции предоставляют один или несколько методов для получения
    новых экземпляров итератора, совместимых с классом коллекции.
    """

    def __init__(self, collection=[]):
        self._collection = collection

    def __iter__(self):
        """
        Метод __iter__() возвращает объект итератора, по умолчанию мы возвращаем
        итератор с сортировкой по возрастанию.
        """
        return ConcreteIterator(self._collection)

    def get_reverse_iterator(self):
        return ConcreteIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


collection = Collection()

collection.add_item("1")
collection.add_item("2")
collection.add_item("3")

print("Прямой порядок:")
print(", ".join(collection))
print("Обратный порядок:")
print(", ".join(collection.get_reverse_iterator()))
