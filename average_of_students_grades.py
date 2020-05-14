with open("test.txt", "r", encoding='utf-8', errors='ignore') as f:
    lines = f.read()

lines = lines.splitlines()
matrix = [list(map(int, list(filter(lambda z: z.isdigit(), x.split(';'))))) for x in lines]

for row in matrix:
    print(sum(row)/len(row))

[print(float(sum(l)) / len(l), end=" ") for l in zip(*matrix)]
