def process_numbers(n):
    if n == 0:
        return "Программистов"
    elif n == 1:
        return "Программист"
    elif 1 < n < 5:
        return "Программиста"
    else:
        return "Программистов"


def say_number_of_programmers_with_proper_ending(n):
    two_digit_number = str(n)[-2:]
    if int(two_digit_number) > 19:
        number_to_process = two_digit_number[-1:]
    else:
        number_to_process = two_digit_number
    return str(n) + " " + process_numbers(int(number_to_process))

    # 0 программистов
    # 1 программист

    # 2 программиста
    # 3 программиста
    # ..

    # 5 программистов
    # ...
    # 20 программистов

    # 21 программист


print(say_number_of_programmers_with_proper_ending(15))
