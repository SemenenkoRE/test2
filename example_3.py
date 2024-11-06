

class MySequence:

    def __init__(self, finish_numb):
        self.finish_numb = finish_numb

    def __iter__(self):                    # Вызывается при вызове метода iter()
        self.numb = 1                      # Создается начальное значение выдаваемых итератором значений
        print('Вызван __iter__')
        return self                        # Возращает сам себя

    def __next__(self):                    # Вызывается при вызове метода next()

        if self.numb < self.finish_numb:

            x = self.numb                      # Следующее возращаемое значение, передающееся посредством переменной x
            self.numb += 1                     # Изменить следующее выдаваемое значение, которое будет применено в следующей итерации
            print('Вызван __next__')
            return x                           # Вернуть возращаемое значение, хранящийся в перемнной x

        else:
            raise StopIteration

seq = MySequence(4)
my_iter = iter(seq)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
