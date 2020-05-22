from decorators import do_twice, timer


@do_twice
def greeting(name):
    print(f"Hello {name}")
    return "Hello " + name


greeting("Roman")


@timer
def waste_some_time(iterations):
    for _ in range(iterations):
        sum([i**2 for i in range(10000)])


waste_some_time(10)
waste_some_time(100)
waste_some_time(1000)
waste_some_time(10000)
