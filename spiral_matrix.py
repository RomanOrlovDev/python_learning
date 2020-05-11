row = 0  # row start point
column = 0  # column start point
numbers = 1  # numbers in matrix
square_length = int(input())  # square length to be filled
reverse = False  # define direction of numbers filling
matrix = [[0 for x in range(square_length)] for y in range(square_length)]

while True:
    x = column
    # row filling
    while True:
        if not matrix[row][x]:
            matrix[row][x] = numbers
            numbers += 1
        if reverse:
            if x == column - square_length + 1:
                break
            x -= 1
        else:
            if x == column + square_length - 1:
                break
            x += 1
    column = x
    x = row
    # column filling
    while True:
        if not matrix[x][column]:
            matrix[x][column] = numbers
            numbers += 1
        if reverse:
            if x == row - square_length + 1:
                break
            x -= 1
        else:
            if x == row + square_length - 1:
                break
            x += 1
    row = x
    if reverse:
        square_length -= 2
        row += 1
        column += 1

    if square_length < 1:
        break

    reverse = not reverse

for rows in matrix:
    for columns in rows:
        print(columns, end="\t")
    print()
