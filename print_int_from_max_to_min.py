def print_int_from_max_to_min(a, b, c):
    my_arr = [a, b, c]
    my_arr.sort(key=None, reverse=True)
    for i in range(3):
        print(my_arr[i])


print_int_from_max_to_min(2, 8, 12)
