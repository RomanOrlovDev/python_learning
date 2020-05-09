import random

random_set = set()
while True:
    random_value = random.randint(0, 10)
    if random_value in random_set:
        break

    random_set.add(random_value)

print(len(random_set) + 1)
print(random_set)
print(random_value)
