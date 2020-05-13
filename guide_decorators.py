# what is decorator
# is it possible to decorate with two decorators (spec. via commentaries)
# what if *args, **kwargs are interchanged

# def decorator(func):
#     return func
#
#
# @decorator
# def decorated():
#     print("Hello")
#
#
# decorated = decorator(decorated)

import functools


def decorator(func):
    def new_func():
        pass
    return new_func


@decorator
def decorated():
    print("Hello")


# decorated = decorator(decorated)
decorated()

print(decorated.__name__)

log = []


def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        f = open("test.txt", "a")
        f.write(str(result) + "\n")
        f.close()
    return wrapped


@logger
def summator(new_list):
    return sum(new_list)

summator([2, 3, 444])
with open("test.txt", "r") as f:
    print("test.txt: ", f.read())
