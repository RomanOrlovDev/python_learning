n, m = [int(x) for x in input().split()]
stars = [(i, j) for i in range(n) for j, c in enumerate(input()) if c == '*']

for i in range(n):
    for j in range(m):
        if (i, j) in stars:
            print('*', end='')
        else:
            count_of_stars_around = 0
            for y in (j - 1, j, j + 1):
                for x in (i - 1, i, i + 1):
                    if (x, y) in stars:
                        count_of_stars_around += 1
            print(count_of_stars_around, end='')
    print()


###
n, m = [int(i) for i in input().split()]
field = [[0 for i in range(m + 2)] for j in range(n + 2)]
for i in range(n):
    a = input()
    for j in range(m):
        if a[j] == '*':
            field[i + 1][j + 1] = '*'

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if field[i][j] != '*':
            if field[i][j + 1] == '*': field[i][j] += 1
            if field[i][j - 1] == '*': field[i][j] += 1
            if field[i + 1][j] == '*': field[i][j] += 1
            if field[i - 1][j] == '*': field[i][j] += 1
            if field[i + 1][j + 1] == '*': field[i][j] += 1
            if field[i + 1][j - 1] == '*': field[i][j] += 1
            if field[i - 1][j + 1] == '*': field[i][j] += 1
            if field[i - 1][j - 1] == '*': field[i][j] += 1

for i in field[1:-1]:
    print(*i[1:-1], sep='')
# @Vladyslav_Balan, все эти "if"ы реализуются через цикл для k от 0 до 9, где [i+k//3-1] [j+k%3-1]