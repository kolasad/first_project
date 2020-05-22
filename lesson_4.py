

sentence = 'Ala ma kota. Maciej nie ma kota.'
sentence2 = 'Ala ma kota. Maciej nie ma psa.'


def count_animals(word):
    return word.count('kot') + word.count('psy') + word.count('pies') + word.count('psa')


assert count_animals(sentence) == 2
assert count_animals(sentence2) == 2


# calculate value of products with discount possibility

def calculate_value(products_prices):
    """
    Calculates value of all products including discount
    :param products_prices: list of prices
    :return: sum of prices with discount included
    """
    price = sum(products_prices)
    discount = 0
    if price > 500:
        discount = 20
    elif price > 100:
        discount = 10
    price -= (price * discount) / 100
    return round(price, 2)


# arguments - args
def calculate_values(*args):
    # first_argument = args[0]
    # print(first_argument)
    numbers = [x for x in args if isinstance(x, int) or isinstance(x, float)]
    products_sum = sum(numbers)
    products_names = [x for x in args if isinstance(x, str)]
    return {
        'names': products_names,
        'products_sum': products_sum
    }


# key word arguments - kwargs
def calculate_value_with_defined_discount(products_prices, discount=None):
    """
    Calculates value of all products including discount which can be defined or calculated based on products value
    :param discount: value of discount
    :param products_prices: list of prices
    :return: sum of prices with discount included
    """
    price = sum(products_prices)
    if discount is None:  # first step: if there is no discount I calculate discount based on products value
        discount = 0
        if price > 500:
            discount = 20
        elif price > 100:
            discount = 10

    if discount > 80:
        discount = 80

    price -= (price * discount) / 100
    return round(price, 2)


# kwargs
def calculate_values_with_kwargs(*args, **kwargs):
    sum_args = args[0] + args[1]
    name_args = args[2]
    sum_kwargs = kwargs['product_price']
    name_kwargs = kwargs.get('product_name')
    return {
        'names': [name_args, name_kwargs],
        'products_sum': [sum_args, sum_kwargs]
    }
