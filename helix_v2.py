n = int(input())
matrix = [[0] * n for i in range(n)]
index = 1
top = 0

matrix[n // 2][n // 2] = n * n

for vertical in range(n // 2):

    for i in range(n - top):
        matrix[vertical][i + vertical] = index
        index += 1
    for i in range(vertical + 1, n - vertical):
        matrix[i][-vertical - 1] = index
        index += 1
    for i in range(vertical + 1, n - vertical):
        matrix[-vertical - 1][-i - 1] = index
        index += 1

    for i in range(vertical + 1, n - (vertical + 1)):
        matrix[-i - 1][vertical] = index
        index += 1

    top += 2


for rows in matrix:
    for columns in rows:
        print(columns, end="\t")
    print()

