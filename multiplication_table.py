a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(" ", end=" ")
for x in range(c, d+1):
    print(int(x), end=" ")

print(" ")
for x in range(a, b+1):
    print(x, end=" ")
    for y in range(c, d+1):
        print(x*y, end=" ")
    print("")

