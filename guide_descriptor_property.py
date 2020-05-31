class Property:
    __slots__ = ['getter']

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        print('''getter called''')
        if instance is None:
            return self

        return self.getter(instance, 13)


class Account:

    @Property
    def add_tax(self, tax):
        return 'tax added: {}'.format(tax)

    def add_simple_tax(self, tax):
        return 'simple tax added: {}'.format(tax)

    add_simple_tax = Property(add_simple_tax) # this is the same as @Property marking

t = Account()
print(t.add_tax)
print(t.add_simple_tax)
# t.add_simple_tax
