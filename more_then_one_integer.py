lst = input().split()

print(*[e for e in set(lst) if lst.count(e) > 1])

# Время: не  дождался)

d = dict()
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    if d[i] > 1:
        print(i, end=' ')
# Время: 3.2439730167388916

lst = sorted(lst)
for i, j in groupby(lst):
    if len(list(j)) > 1:
        print(i, end=' ')
# Время: 7.661556005477905

res = Counter(lst)
for it in res.keys():
    if res[it] > 1:
        print(it, end=' ')
# Время: 3.404210090637207

lst.sort()
for i in range(1, len(lst) - 1):
    if lst[i] != lst[i + 1] and lst[i] != lst[i - 1]:
        lst[i] = None
        lst[0], lst[-1] = None, None
print(*[lst[x] for x in range(1, len(lst)) if (lst[x] is not None and lst[x] != lst[x - 1])])
# Время: 6.667062997817993