import functools
import time


def do_twice(func):
    def wrapper_func(*args, **kwargs):
        print("wrapper start")
        m = func(*args, **kwargs)
        n = func(*args, **kwargs)
        print("returned values are", m, n)
        print("wrapper end")
    return wrapper_func


def timer(func):
    """Benchmark"""
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        finish_time = time.perf_counter()
        run_time = finish_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_func

