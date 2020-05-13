# списочные выражения

# список чисел в квадрате
my_list = [x ** 2 for x in range(5)]
print(my_list)

# список только чётных чисел
even_list = [x for x in range(11) if x % 2 == 0]
print(even_list)

# Также можно писать dict comprehensions
square_map = {num: num ** 2 for num in range(5)}
print(square_map)

reminders_set = {num % 10 for num in range(100)}
print(reminders_set)
