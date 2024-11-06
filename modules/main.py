
class Figure:

    def __init__(self):
        self.area = None
        self.calc_area()

    def __add__(self, other):
        result = Figure()
        result.area = self.area + other.area
        return result

    def calc_area(self):
        self.area = 0

class Circle(Figure):

    def __init__(self, r):
        # super().__init__()
        # self.area = None
        self.r = r
        self.calc_area()
        super().__init__()

    def calc_area(self):
        self.area = 3.14 * self.r ** 2
        print(f'area circle: {self.area}')

class Box(Figure):

    def __init__(self, a, b):
        # super().__init__()
        # self.area = None
        self.a = a
        self.b = b
        self.calc_area()
        super().__init__()

    def calc_area(self):
        self.area = self.a * self.b
        print(f'area box: {self.area}')

    
circle_1 = Circle(10)
box_1 = Box(3, 4)
circle_2 = Circle(5)

print(circle_1 + box_1 + circle_2)