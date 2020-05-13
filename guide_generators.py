def even_generator(start, end):
    while start < end:
        yield start
        start += 2


for number in even_generator(0, 10):
    # print(type(number)) <-- class 'int'
    print(number)

t = even_generator(0, 10)
print(next(t))

