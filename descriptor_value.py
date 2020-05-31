class Value:
    # def __init__(self):
    #     self.computed_amount = 0

    def __set__(self, instance, value):
        self.computed_amount = value - instance.commission * value

    def __get__(self, instance, owner):
        return int(self.computed_amount)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)
