# this is unordered array of unique values
import random

random_set = set()
another_set = {}

while True:
    random_value = random.randint(0, 10)
    if random_value in random_set:
        break

    random_set.add(random_value)

print(len(random_set) + 1)
print(random_set)
print(random_value)


some_set = {2, 3, 5, 5}
some_set.add(5)
print(some_set)
# some_set[1] = 23 <-- not allowed