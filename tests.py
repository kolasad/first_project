from lesson_4 import (
    calculate_value, calculate_values, calculate_value_with_defined_discount,
    calculate_values_with_kwargs
)

products = [1.99, 3.45, 9.99, 34.99]
products_2 = [99.99, 32.49, 9.99, 34.99]
products_3 = [99.99, 32.49, 1399.00, 34.99]

products_price = calculate_value(products)
assert products_price == 50.42
products_price = calculate_value(products_2)
assert products_price == 159.71
products_price = calculate_value(products_3)
assert products_price == 1253.18


result = calculate_values(1, 20, 3, 'Gold', 100.00, 'Pet', 'Shoes', 20)
assert result == {'names': ['Gold', 'Pet', 'Shoes'], 'products_sum': 144.0}


result = calculate_value_with_defined_discount(products, 50)
assert result == 25.21
result = calculate_value_with_defined_discount(products, discount=200)
assert result == 10.08
result = calculate_value_with_defined_discount(products)
assert result == 50.42
result = calculate_value_with_defined_discount(products_2)
assert result == 159.71


result = calculate_values_with_kwargs(40000, 100000, 'Mercedes', product_name='BMW', product_price=80000)
assert result == {'names': ['Mercedes', 'BMW'], 'products_sum': [140000, 80000]}
