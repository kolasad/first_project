# 1
# Write a function which takes name as argument and when called returns a sentence with that name
# For example given the name: Marek
# Function should return: 'Hello Marek, how are you?'


def write_sentence(name):
    return f'Hello {name}, how are you?'


names = ['Marek', 'Jan', 'Dominik']
for name in names:
    assert write_sentence(name) == f'Hello {name}, how are you?'


# 2
# Write a function taking multiple arguments and
# a) returning a list of arguments passed  to that function in a list.
# b) returning a list of arguments, but takes only floats and integers
# c) returning a list of arguments, but takes only strings
# d) returning a tuple with list of floats and integers arguments and list of strings arguemnts

def multiple_arguments_func(*args):
    return list(args)


assert multiple_arguments_func('a', 1, 23) == ['a', 1, 23]
assert isinstance(multiple_arguments_func('a', 1, 23), list)


def multiple_arguments_func(*args):
    numbers = []
    for argument in args:
        if isinstance(argument, float) or isinstance(argument, int):
            numbers.append(argument)
    return numbers


assert multiple_arguments_func('a', 1, 23, '123 ', 1020, 129039123.12030123) == [1, 23, 1020, 129039123.12030123]


def multiple_arguments_func(*args):
    strings = []
    for argument in args:
        if isinstance(argument, str):
            strings.append(argument)
    return strings


assert multiple_arguments_func('a', 1, 23, '123 ', 1020, 129039123.12030123) == ['a', '123 ']


def multiple_arguments_func(*args):
    numbers = []
    strings = []
    for argument in args:
        if isinstance(argument, float) or isinstance(argument, int):
            numbers.append(argument)
        elif isinstance(argument, str):
            strings.append(argument)
    return numbers, strings  # tuple(numbers, strings)


assert multiple_arguments_func('a', 1, 23, '123 ', 1020, 129039123.12030123) == (
    [1, 23, 1020, 129039123.12030123], ['a', '123 '])

# 3
# Write a function taking float value and calculating tax for it
# assume that tax is 18 % bu up to 80 000 and for the rest value above
# 80 000 tax amount is 32 %
# b) include social donations, set the kwarg in that function called: children_count
# default value should be 0, if children count is provided then you
# subtract 300 from the values of tax. Remember that tax can't be lower then 0


def calculate_tax(amount):
    if amount > 80000:
        first_tax = 80000 * 0.18
        second_tax = (amount - 80000) * 0.32
        return first_tax + second_tax
    else:
        return amount * 0.18


assert calculate_tax(50000) == 9000.0
assert calculate_tax(80000) == 14400.0
assert calculate_tax(120000) == 27200.0


def calculate_tax(amount, children_count=0):
    if amount > 80000:
        first_tax = 80000 * 0.18
        second_tax = (amount - 80000) * 0.32
        tax = first_tax + second_tax
    else:
        tax = amount * 0.18
    donation = children_count * 300
    tax -= donation  # tax = tax - donation
    if tax < 0:
        return 0
    return tax


assert calculate_tax(50000) == 9000.0
assert calculate_tax(80000, children_count=1) == 14100.0
assert calculate_tax(120000, children_count=3) == 26300.0

# 4
# Write a function which takes multiple key word arguments and prints them
# alphabetically to console based on keys
# b) print them alphabetically reversed


def print_kwargs(**kwargs):
    arguments = []
    for key, value in kwargs.items():
        arguments.append((key, value))
    arguments.sort(key=lambda x: x[0])
    # arguments.sort(key=lambda x: x[0], reverse=True)  # b reversed
    print(arguments)


print_kwargs(number=1090, sentence='Hello everyone', A='A')

# 5
# Write a function which will write to a file 'logs.txt' the value of arguments
# and key word arguments passed to that function


def log(*args, **kwargs):
    with open('logs.txt', 'w') as file:
        for argument in args:
            file.write(str(argument))
            file.write('\n')
        for kwarg in kwargs:
            file.write(str(kwarg))
            file.write('\n')


log(1, 2, 3, 'Sentence', number=1090, sentence='Hello everyone', A='A')
