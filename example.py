class Figure:

    def __init__(self):
        self.area = None

    def __add__(self, other):
        return self.area + other.area

    def __lt__(self, other):
        try:
            if isinstance(other, Circle) or isinstance(other, Box):     # если тип объекта соответстует Circle или Box
                return self.area < other.area
            else:                                                       # если все остальные объекты, которые возможно чиленно сравнить
                return self.area < other

        except Exception as ex:
            return ex                                                   # вернет формулировку ошибки


class Circle(Figure):

    def __init__(self, r):
        super().__init__()
        self.r = r
        self.calc_area()

    def calc_area(self):
        self.area = 3.14 * self.r ** 2
        print(f'area circle: {self.area}')


class Box(Figure):

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.calc_area()

    def calc_area(self):
        self.area = self.a * self.b
        print(f'area box: {self.area}')


circle_1 = Circle(10)
box_1 = Box(3, 4)

print(circle_1 < box_1)
print(circle_1 < 500)
print(circle_1 < '333')
