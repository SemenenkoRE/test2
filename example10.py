
class SimpleClass:

    def __init__(self, **kwargs):

        for key, val in kwargs.items():
            setattr(self, key, val)         # при варианте создания атрибута через setattr будет выполнен __setattr__

    def __setattr__(self, key, value):

        print('changes')

        super().__setattr__(key, value)

simple_obj = SimpleClass(**{'attr_1': 1, 'attr_2': 2})

# print(simple_obj.__dict__)

simple_obj.attr_3 = '3'             # при варианте прямого создания атрибута объекта будет выполнен __setattr__
simple_obj.attr_3 = 'new 3'         # при изменении атрибута объекта также будет выполнен __setattr__