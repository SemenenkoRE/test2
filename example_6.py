
class Figure:


    def __init__(self, *args, **kwargs):

        # *args, **kwargs - это паттерн проектирования, который позволяет передвать дочерним объектам что угодно
        # даже если сейчас это не нужно

        self.area = 0

    @classmethod
    def create_instance(cls, *args):

        # Один из основных функционалов classmethod:
        # create_instance - фабрика объектов, котоая вместе с созданием объекта может выполнять какую либо
        # дополнимтельную бизнес-логику. Далее элементарный пример условного уведомления о создании объекта.

        print(f'{cls.__name__}: {args}')

        # cls - это название класса, в котором обращаются к данному методу
        # *args - это способ передачи аргументов позиционным параметрам функции, количество и смысл которых
        # для разных дочерних объектов будет разным

        return cls(*args)

class Circle(Figure):

    """ Фигура: круг """

    def __init__(self, r):
        self.r = r
        self.calc_area()
        super().__init__()

    def calc_area(self):
        self.area = 3.14 * self.r ** 2
        print(f'area circle: {self.area}')


class Box(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.calc_area()
        super().__init__()

    def calc_area(self):
        self.area = self.a * self.b
        print(f'area box: {self.area}')


circle_1 = Circle.create_instance(10)
box_1 = Box.create_instance(5, 20)

print(Figure.__name__)
print(circle_1.__dict__)
print(circle_1.__class__.__name__)

# print(Circle.__doc__)

# print(isinstance(circle_1, Circle))
#
# print(circle_1.__class__)
# print(circle_1.__class__.__bases__)
# print(Figure.__dict__)



