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
        # fill the matrix cell only if it is not filled yet
        if not matrix[row][x]:
            matrix[row][x] = numbers
            numbers += 1

        if reverse:  # go from right to left
            if x == column - square_length + 1:
                break
            x -= 1
        else:  # go from left to right
            if x == column + square_length - 1:
                break
            x += 1
    column = x  # store last applied column value

    x = row
    # column filling
    while True:
        # fill the matrix cell only if it is not filled yet
        if not matrix[x][column]:
            matrix[x][column] = numbers
            numbers += 1

        if reverse:  # go down up
            if x == row - square_length + 1:
                break
            x -= 1
        else:  # go top down
            if x == row + square_length - 1:
                break
            x += 1
    row = x  # store last applied row value

    if reverse:  # we have completed the whole contour, it's time to go to inner square
        square_length -= 2
        row += 1
        column += 1

    if square_length < 1:
        break

    reverse = not reverse  # each time when we gone 2 sides of square need to change direction of iteration

for rows in matrix:
    for columns in rows:
        print(columns, end="\t")
    print()


# n = int(input())
# l = [[n * n] * n for _ in range(n)]
# t = list(range(n * n, 0, -1))
# for lo, hi in enumerate(range(n - 1, n // 2 - 1, -1)):
#     for x in range(lo, hi):
#         l[lo][x] = t.pop()
#     for y in range(lo, hi):
#         l[y][hi] = t.pop()
#     for x in range(hi, lo, -1):
#         l[hi][x] = t.pop()
#     for y in range(hi, lo, -1):
#         l[y][lo] = t.pop()
# for row in l:
#     print(' '.join(map(str, row)))
