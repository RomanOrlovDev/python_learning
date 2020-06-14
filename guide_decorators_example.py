import time

log_container = []


def logger(my_original_func):

    def method_with_arbitrary_name(*args, **kwargs):  # это функция обёртка,
        # она ВСЕГДА нужна чтобы корректно обернуть оригинальную функцию - это надо просто запомнить
        # обычно эту функцию обёртку называют def wrapper(...) - я её переименовал для более точного понимания

        print("DECORATOR RUN_TIME")  # этот принт добавлен для понимания,
        # что декораторы управляют вызовом оригинальной функции
        # вызов оригинальной функции это вызов my_original_func(*args, **kwargs) ниже

        local_container = list()
        local_container.append('******** LOG OF: ' + my_original_func.__name__ + ' ********')
        initial_time_point = time.time()
        local_container.append("Started at: " + str(time.ctime()))

        # вызов оригинальной функции (в нашем случае func1 или another_function)
        my_original_func(*args, **kwargs)

        end_time_point = time.time()
        local_container.append("Finished at: " + str(time.ctime()))
        local_container.append("It took (seconds) " + str(end_time_point - initial_time_point))
        local_container.append('********* END OF LOG ********')
        log_container.append("\n".join(local_container))

        print("END OF DECORATOR RUN TIME")   # этот принт добавлен для понимания,
        # что декораторы управляют вызовом оригинальной функции
        # вызов оригинальной функции это вызов my_original_func(*args, **kwargs) выше

        print("\n")

    return method_with_arbitrary_name


@logger
def func1():
    print("Hello this is func1, let's start")
    print("Below I will make small amount of operations, so I will not make you wait")
    i = 0
    while i < 200000:
        i += 1
    print("I have finished my job (this is func1)")


@logger
def another_function():
    print("Hello this is func2, let's start")
    print("Below I will make a lot of computations, please be patient")
    i = 0
    while i < 30000000:
        i += 1
    print("I have finished my job, hope it wasn't too much long (this is another_function)")


func1()
another_function()

# на самом деле вызов этих двух функций сверху можно заменить на:
# func1 = logger(func1)
# func1()
#
# another_function = logger(another_function)
# another_function()
# только нужно удалить пометку @logger из этих функций предварительно

print(*[i + "\n\n" for i in log_container])
