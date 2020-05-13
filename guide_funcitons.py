# comments inside functions - this will be stored in a special property function_name.__doc__
# function name is stored in special name function_name.__name__
# if no return then None will be returned
# types of parameters can be annotated: some_function(a: int, b: int)
# keywords arguments (именнованные аргументы) - определяют параметры и их значения для функций. Н-р:
# def say(greeting, name)
# say(name="Kitty", greeting="Hello") <--- this will work correctly
# arguments with default values supported
# arguments could be passed as tuple so we would not know how many arguments were passed to function, e.g.:
# some_func(*args):
# print(type(args)) <--- <class 'tuple'>
# for argument in args:
# print(argument)
# some_func(*some_arguments) some_arguments has to be a list
# some_func(**some_arguments) some_arguments has to be a dict

def some_function(greeting, name="Anatoly"):
    """this is very first function here"""
    return greeting + " " + name

print(some_function.__doc__)
print(some_function(name="Kitty", greeting="Hello"))
print(some_function("Hi"))


def some_another_function_(*args):
    print("this is some_another_function_")
    for a in args:
        print(a)


def some_another_function2(*args):
    print("this is some_another_function2")
    for a in args:
        print(a)


some_another_function_(1, 5, 6)


simple_list = ['asdf', 'qwer']
some_another_function2(*simple_list)  # <--- asterisk is important


def some_another_function3(**this_will_be_dict):  # <--- this will become dictionary
    print("this is some_another_function3: ")
    print(type(this_will_be_dict))
    for key, val in this_will_be_dict.items():
        print('{}: {}'.format(key, val))


some_another_function3(a=12, test="asdf", x=88)


def some_another_function4(**dictionary_arg):
    print("this is some_another_function4")
    print(dictionary_arg)


obj_example = {
    'user_id': 3,
    'description': 'nice to meet you'
}
some_another_function4(**obj_example)  # <--- two asterisks are important
