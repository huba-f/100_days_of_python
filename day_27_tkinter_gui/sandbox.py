def add(*args):
    print(type(args))
    sum_of_args = 0
    for n in args:
        sum_of_args += n
    return sum_of_args


print(add(2, 4, 6, 3, 5, 6, 7, 7, 8))


def calculate(n, **kwargs):
    print(type(kwargs))
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(3, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')


my_car = Car(make='Tesla', model='Model S')
print(my_car.make)
print(my_car.model)
