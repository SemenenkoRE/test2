class Figure:

    def __init__(self):
        self._perimeter = None

    @property
    def perimeter(self):                # далее данное название функции будет повторятся
        print('This is GETTER')
        return self._perimeter

    @perimeter.setter
    def perimeter(self, value):         # тоже название, что и у функции для геттера
        print('This is SETTER')
        self._perimeter = value

    @perimeter.deleter
    def perimeter(self):                # тоже название, что и у функции для геттера
        print('This is DELETER')
        del self._perimeter


fig = Figure()

fig.perimeter = 10
print(fig.perimeter)
del fig.perimeter