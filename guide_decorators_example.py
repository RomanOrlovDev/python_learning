import time


"""Декорация - это паттерн (т.е. приём), который используется во многих языках. Его цель - добавить дополнительной функциональности в метод (или в класс или ещё в какую-то программную единицу). 
Возникает вопрос: почему просто нельзя добавить дополнительный код в метод, чтобы этот метод делал то, что от него требуют. Ответ простой - теоритически можно, но на практике это засрёт код и сделает его неподдерживаемым. 

Пример:

У нас большой проект, который в какой-то момент начинает дико тормозить. Нужно делать анализ системы, находить куски кода, которые выполняются очень долго. Такой анализ обычно делают с помощью нескольких инструментов. Один из таких инструментов - добавить логирование в методы, которые находятся под подозрением. Вот добавление такого логирования можно сделать красиво с помощью декораторов. Мы пишем один декоратор, который записывает время начала выполнения метод, имя метода и время окончания выполнения метода. И этот декоратор применяем ко многим методам системы. 

В Питоне это выглядит примерно так:

@some_custom_decorator
def some_function()

важно понимать, что @some_custom_decorator - это просто сахар Питона. 
На самом деле здесь происходит вот такая простая последовательность действий: 
some_function = some_custom_decorator(some_function)
some_function()

На практике это будет выглядеть примерно так:

Кстати декорировать можно сколько угодно много разными декораторами:

@some_custom_decorator
@another_custom_decorator
def some_function()

здесь сначала будет вызывана функция some_custom_decorator, внутри неё отработает some_function и результат будет передан декоратору another_custom_decorator который также вызовет some_function"""

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
