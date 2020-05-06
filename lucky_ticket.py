f = input()


def check_if_the_ticket_is_lucky(ticket_number):
    if len(ticket_number) != 6:
        return "Номер билет должен содержать ровно шесть знаков"
    # ticket_number = [1, 2, 3]
    if sum(map(lambda x: int(x), list(ticket_number[0:3]))) == sum(map(lambda x: int(x), list(ticket_number[3:6]))):
        return "Счастливый"
    else:
        return "Обычный"


print(check_if_the_ticket_is_lucky(f))
