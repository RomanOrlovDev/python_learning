rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
to_check = input()

v = 0
for i in range(len(to_check)):
    if i + 1 == len(to_check):
        v += rom[to_check[i]]
    else:
        if rom[to_check[i + 1]] > rom[to_check[i]]:
            v -= rom[to_check[i]]
        else:
            v += rom[to_check[i]]

print(v)
