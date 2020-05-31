class Logger:
    __slots__ = ['amount']

    def __init__(self, amount):
        self.amount = amount

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, value):
        with open('some_file.txt', 'a') as f:
            f.write(str(value))
        self.amount = value


class Account:
    amount = Logger(200)


t = Account()
t.amount = 300

with open("some_file.txt", "r") as r:
    print(r.read())
