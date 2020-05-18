empty = None
# boolean
true_example = True
false_example = False

# numbers: integer, float
int_example = 2
float_example = 2.34

# string
string_example = 'Ala ma kota.'

# collections: list, tuple, dictionary
list_example = [1, 2, 3, 'Jan']
tuple_example = (1, 2, 3, 'Jan')  # can't change tuple
dictionary_example = {1: 'Asia', 'Jan': 2, 'key': 'value'}

print(dictionary_example)

# tuple_example[0] = 10  # U can't change the tuple

# print(type(list('asdd')))
# print(list('asdd'))

# Zmiana typow
print(float_example)
int_as_string = str(float_example)
print(float_example)

first_number = int_as_string[:1]
string_as_int = int(first_number)
string_as_float = float(int_as_string)

# split string
print(int_as_string.split('.'))

print(0.3 + 0.3 + 0.33)

# get n first elements of list
print(f'Lista: {list_example}')
print('Lista: {}'.format(list_example))
print('Lista: %s' % list_example)
n = 2
print(list_example[:n])
list_example[0] = 10
print(list_example)
# add to list
list_example.append('kot')
print(list_example)
# Sort list
unsorted_list = [1, 5, 7, 2, 4, 1]
unsorted_list.sort()
print(unsorted_list)

# remove item from list
del unsorted_list[4]
print(unsorted_list)

unsorted_list[2] = 'Jan'
print(unsorted_list)
unsorted_list[2] = [1, 2, 10, 1]
print(unsorted_list)
print(unsorted_list[2][2])

print(f'Dictionary: {dictionary_example}')
print(dictionary_example['key'])
print(dictionary_example.get('key'))  # the same as line above, but checks if key is in dict
print(dictionary_example[1])

# print(dictionary_example['Nowak'])  # error, no such key in dictionary_example

key_value = dictionary_example.get('key')
print(key_value)
key_value = dictionary_example.get('Nowak')  # when there is no such key, None is returned
print(key_value)

key_value = dictionary_example.get('Nowak', 120)  # when there is no such key, default value is returned
print(key_value)

poped_value = dictionary_example.pop('key')
print(poped_value)
print(dictionary_example)

# get dict items, keys, values
print(dictionary_example.items())
print(dictionary_example.keys())
print(dictionary_example.values())

# change dict_keys type to list to get first element
print(list(dictionary_example.keys())[0])

dictionary_example['first_name'] = 'Adam'
print(dictionary_example)
dictionary_example['last_name'] = 'Nowak'
print(dictionary_example)
dictionary_example['last_name'] = 'Kowalski'
print(dictionary_example)

users = [
    {
        "last_name": "Nowak",
        "first_name": "Adam"
    },
    {
        "last_name": "Kowalski",
        "first_name": "Jan"
    },
    {
        "last_name": "Lewandowski",
        "first_name": "Rafal"
    },
]


#  wybrac pierwszego uzytkownika z listy users
#  wybrac pierwsze imie drugiego uzytkownika
#  wybrac klucze ostatneigo uzytkownika
#  dodac nowego uzytkownika
#  usunac pierwszego uzytkownika
#  zmienic imie i nazwisko ostatniego uzytkownika

print(users[0])
second_user = users[1]
print(second_user)
print(type(second_user))
second_user_first_name = second_user['first_name']
print(second_user_first_name)

user_keys = users[2].keys()
print(user_keys)

new_user = {
    "last_name": "Nowak",
    "first_name": "Asia"
}
users.append(new_user)
print(users)

del users[0]

print(users)

print(users[2])
users[2]['last_name'] = 'Kowalski'
users[2]['first_name'] = 'Agata'

print(users)
