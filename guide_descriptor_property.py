class Property:
    __slots__ = ['getter']

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        print('''getter called''')
        if instance is None:
            return self

        return self.getter(instance)


class Account:

    @Property
    def add_tax(self):
        return 'tax added'

    def add_simple_tax(self):
        return 'simple tax added'

    add_simple_tax = Property(add_simple_tax) # this is the same as @Property marking

t = Account()
print(t.add_tax)
print(t.add_simple_tax)
# t.add_simple_tax
