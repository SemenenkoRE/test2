
def make_gen(finish_numb):

    for num in range(finish_numb):
        yield num

gen = make_gen(3)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# def simple_generator():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
# gen = simple_generator()
#
# print(next(gen))
# print(next(gen))
# print(next(gen))

