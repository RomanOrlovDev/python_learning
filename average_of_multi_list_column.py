import random
column = 2


def get_average(column):
    matrix = [[random.randint(1, 10) for x in range(random.randint(0, 10))] for y in range(random.randint(1, 10))]
    sum = 0
    counter = 0
    for row in matrix:
        if len(row) >= column:
            sum += row[column-1]
            counter += 1

    print(matrix)
    print(sum)
    print(counter)
    if counter:
        print(sum/counter)
    print("THE END")


for x in range(1000):
    get_average(column)
