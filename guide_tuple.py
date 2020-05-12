# tuple or korteji - is immutable list
# this is ordered array as well as lists
# unlike set
empty_tuple = ()
empty_tuple = tuple()
immutable_types = (int, str, list)

print(immutable_types)

# objects inside tuples could be changed
blink = ([], [])
blink[0].append('new value for the first list')

print(blink)

# hash can be applied to tuples
print(hash(tuple()))
print(hash((2, 5)))

