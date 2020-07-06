n = int(input())
i, j = 1, 1
for _ in range(1, n + 1):
    print(i)
    j -= 1
    if not j:
        i += 1
        j = i

# print(*[i for i in range(1, n+1)])
# i = 3
# while i > 0:
#     j = 2
#     while j > 0:
#         print("i{}: j{}".format(i, j))
#         j -= 1
#         if i == 2:
#             break
#     i -= 1

# iterable_number = 1
# while True:
#     for i in range(1, iterable_number+1):
#         print(i)
#         n -= 1
#         if n == 0:
#             break
