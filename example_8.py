class SimpleClass:

    def __init__(self, **kwargs):

        for key, val in kwargs.items():
            setattr(self, key, val)        #

    def __repr__(self):
        return f'Объект класса {self.__class__.__name__}'

    def __

p1 = SimpleClass(**{'name': 'Roman', 'age': 33, 'other_name': None})
p2 = SimpleClass(**{'name': 'Dima', 'age': 30, 'other_name': 'Dimon'})

print(p1)                      # возвращает строковое представление сразу
print(repr(p1))                # возвращает строковое представление, но выводит с помощью print