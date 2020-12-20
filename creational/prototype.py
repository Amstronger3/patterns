import copy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Зарегистрировать объект"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Отменить регистрацию"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Скопировать объект и обновить словарь внутренних атрибутов"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class SheepDolly:
    def __init__(self):
        self.legs = 4
        self.color = 'white'

    def __str__(self):
        return f'{self.legs}, {self.color}'


some_sheep = SheepDolly()
prototype = Prototype()
prototype.register_object('object', some_sheep)
sheep_kate = prototype.clone('object')
sheep_denis = prototype.clone('object', legs=1, color="black")
print([str(i) for i in (some_sheep, sheep_kate, sheep_denis)])
