import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrap_function():
        start = time.time()
        function()
        stop = time.time()
        print(f"{function.__name__} run time: {stop - start}")

    return wrap_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
