t, t2 = input(), input()

found = False
for i in range(0, len(t)):
    if i + len(t2) > len(t):
        break
    if t[i:i + len(t2)] == t2:
        found = True
        print(i, end=' ')

if not found:
    print(-1)

# another solution from forum
s, b = input(), input()
print(*[i for i in range(len(s)) if s.find(b, i) == i] or [-1])