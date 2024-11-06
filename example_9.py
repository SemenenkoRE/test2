
class SomeSequence:

    def __init__(self, *args, **kwargs):

        self.seq_list = [*args]

        self.seq_dict = kwargs

    def __getitem__(self, item):

        return 'обращаемся к атрибуту'

        return super.__getitem__(self, item)


s = SomeSequence(*[1, 5, 3, 6])

print(s.seq_list)
print(s.seq_dict)

for el in s.seq_list:

    pass
