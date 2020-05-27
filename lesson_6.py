# Decorators
import time
import random


def say_something():
    return 'Say something!'


def print_start_end(func):
    def wrapper():
        print('Start decorating')
        start = time.time()
        result = func()
        time.sleep(random.uniform(0, 1))
        print('Sopped decorating')
        print(f'This function took: {time.time() - start}')
        return result
    return wrapper


# say_something = print_start_end(say_something)
# result = say_something()
# print(result)


@print_start_end  # use print_start_end - the same as lines 16, 17
def say_anything():
    return 'Say anything!'


# print(say_anything())


# decorator arguments
def decorator_with_arguments(multiply):
    def print_start_end(func):
        def wrapper():
            print('Start decorating')
            start = time.time()
            result = func()
            time.sleep(random.uniform(0, 1) * multiply)
            print('Sopped decorating')
            print(f'This function took: {time.time() - start}')
            return result
        return wrapper
    return print_start_end


@decorator_with_arguments(2)  # use print_start_end - the same as lines 16, 17
def say_anything():
    return 'Say anything!'


# say_anything()


from functools import wraps


def print_hello(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Hello')
        print(args, kwargs)
        return func(*args, **kwargs)
    return wrapper


def print_bye(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Bye')
        print(args, kwargs)
        return func(*args, **kwargs)
    return wrapper


@print_hello
@print_bye
def say_anything(sentence):
    """Says anything"""
    return f'Say anything! Additional sentence: {sentence}'


# print(say_anything.__doc__)
# print(say_anything.__name__)


# Generators


def my_first_generator(stop):
    value = 0
    while value < stop:
        yield value
        value += 1  # value = value + 1


# generator = my_first_generator(10)
# print(generator.__next__())
# print(next(generator))
# for element in generator:
#     print(element)


def name_generator(name):
    for character in name:
        yield character


# generator = name_generator('Dominik')
# for char in generator:
#     print(char)
#
#
# generator = name_generator('Kinga')
# print([x for x in generator])
#
# generator = name_generator('Kinga2')
# name_table = []
# for x in generator:
#     name_table.append(x)
#
# print(name_table)

# Errors
number = input()
variable = None
try:
    variable = int(number) * 2
except ValueError:
    print('Input valid number!')
finally:
    print('At the end...')


# Catch multiple errors
try:
    variable = int(number) * 2
except (ValueError, AttributeError):
    print('Input valid number!')


# Catch all errors - try not to use broad except Exception !!!
try:
    variable = int(number) * 2
except Exception as e:
    print(f'Input valid number! {e}')
