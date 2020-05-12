some_list = [12, 33, 'a', 39]   # some list defined
another_list = list()  # another way to create a list
# useful methods: min, max, sum, join
# sorted = sorting and creating a new list
# .sort = change list in place

print(3 in some_list)

print(some_list[-1])            # get last element of the list
print(33 in some_list)          # in_array analog

some_second_list = some_list

some_second_list[1] = 34

print(some_list)
print(some_second_list)

some_third_list = some_list[:]
some_third_list[1] = 33
print(some_list)
print(some_third_list)

some_list.append("new value")
some_list.extend(["new_v2", "new_v3"])

some_list += ["new_v4"]
some_list += "new_v5"
print(some_list)

some_new_list = ["boo", "foo", "aa"]
print(", ".join(some_new_list))

some_new_list.sort(reverse=True)
print(some_new_list)

some_tuple = (3, 5,)
print(some_tuple)

some_list = [3, 5, 8, 9, 7, 11]
half_size = len(some_list) // 2
print(some_list[half_size])


