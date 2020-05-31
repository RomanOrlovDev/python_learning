# this extract n from two symbols typed in input separated by whitespace: '22 55'.
# 55 is ignored in such example
n, _ = map(int, input().split())

# this build matrix from input with the format: '1 2 3' \n '4 8 11'
matrix = [input().split() for _ in range(n)]

print(matrix)
print(*matrix)

# zip takes elements from each list
for b in zip(*matrix):
    print(*b)

# another solution that is difficult to grasp, in particular "list" at second line
# n, _ = list(map(int, input().split()))
# list(map(print, *(input().split() for _ in range(n))))
