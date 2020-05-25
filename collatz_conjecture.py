numb = int(input())
print(numb, end=' ')
while 1 != numb:
    numb = numb / 2 if numb % 2 == 0 else numb * 3 + 1
    print(int(numb), end=" ")


# def gen(a):
#     yield a
#     while a != 1:
#         a = a * 3 + 1 if a % 2 else a // 2
#         yield a
#
#
# print(*gen(int(input())))
