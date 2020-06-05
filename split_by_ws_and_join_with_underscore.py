import re

t = 'my      file name.txt'
t = re.sub(r'\s+', r'_', t)
print(t)

t = 'my      file name.txt'
print('_'.join(t.split()))


t = 'my      file name.txt'
print(*t.split(), sep="_")