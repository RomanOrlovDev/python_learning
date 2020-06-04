from collections import Counter
text = input().lower().split()
c = Counter(input().lower().split(' '))
print(c)

my_d = {}
for word in input().split():
    word = word.lower()
    if word not in my_d:
        my_d[word] = 0
    my_d[word] += 1

for word, iter in my_d.items():
    print(word, iter)

# from forum
s = input().lower().split()
for i in set(s):
    print(i, s.count(i))
# [print(i, s.count(i)) for i in set(s)]
