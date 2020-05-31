nm = input().split()
n = int(nm[0])
m = int(nm[1])
c = 0
matrix = []
while c < n:
    matrix.append(list(map(int, input().split())))
    c += 1

# matrix = [[m * row + col + 1 for col in range(m)] for row in range(n)]


def create_property_if_not_exists(matrix, row, col):
    if len(matrix) == row:
        matrix.append([])
    if len(matrix[row]) == col:
        matrix[row].append(None)


def transpose(matrix):
    new_m = []
    for k1, row in enumerate(matrix):
        for k2, col in enumerate(row):
            create_property_if_not_exists(new_m, k2, k1)
            new_m[k2][k1] = col

    return new_m


transposed = transpose(matrix)

for row in transposed:
    for col in row:
        print(col, end=" ")
    print("")

