

class Figure:

    def __init__(self):
        self.area = None

    @staticmethod
    def convert_to_mm(val):     # метод уже не содержит self

        """ Бизнес логика: при необходимости получить результат в милиметрах
        данный метод конвертирует полученное значение в мм """

        return val / 1000


print(Figure.convert_to_mm(3450))