# Lekcja 3
#
# sum_numbers = 1 + 2 * 3 / 1.0
# print(sum_numbers)
#
# sum_numbers = (1 + 2) * 3 / 1.0
# print(sum_numbers)
#
# print(3 % 2)  # modulo
# print(24 % 10)
#
# print(2**2)
# print(2**3)
#
# print('Ala' * 10)
#
# print([1, 2, 3] * 3)
#
# print(3 > 10)
# print(10 > 3)
# print(10 == 14)
# print(10 <= 14)
# print('Python' == 'Python')
#
# import math
#
# print(math.sqrt(9))
#
# # first_number = int(input())
# # second_number = int(input())
# #
# # if first_number > second_number:
# #     print(f'{first_number} is greater than {second_number}')
# # elif second_number > first_number:
# #     print(f'{first_number} is smaller than {second_number}')
# # else:
# #     print('The numbers are equal')
#
# age = 13
# name = 'Jana'
#
# print('Start')
# if age < 18 and name == 'Jan':
#     print('Jan children')
# elif age < 18:
#     print('children')
# elif 18 <= age < 65:
#     print('adult')
# elif age >= 65:
#     print('older person')
# print('End')
#
#
# first_statement = 5 > 4
# second_statement = 1 > 2
# third_statement = 6 > 5
# print(f'({first_statement} and {second_statement}) or {third_statement}')
# print((first_statement and second_statement) or third_statement)
#
# for x in range(10):
#     rest = x % 2
#     if rest == 0:
#         print(f'{x} number')


# Get user email until it's valid
# mail_invalid = True
# while mail_invalid:
#     mail = input()
#     parts = mail.split('@')
#     if len(parts) == 2:
#         domain = parts[1]
#         if '.' in domain:
#             print('Valid mail')
#             mail_invalid = False
#         else:
#             print('Invalid mail, please enter valid one')
#     else:
#         print('Invalid mail, please enter valid one')

# mail_invalid = True
# while mail_invalid:
#     mail = input()
#     parts = mail.split('@')
#     if len(parts) == 2 and '.' in parts[1]:
#         print('Valid mail')
#         mail_invalid = False
#     else:
#         print('Invalid mail, please enter valid one')

# number = 1
# while number < 10:
#     print(number)
#     number += 1  # number = number + 1


# for x in range(10):
#     for y in range(10):
#         print(f'x: {x}, y: {y}')

# number = 1
# while True:
#     print(number)
#     number += 1  # number = number + 1
#     if number % 17.5 == 0:
#         print('break')
#         print(number)
#         break


# names = ['Jan', 'Agata', 'Marcin', 'Dominik', 'Adam']
#
# find = 'Marcin'
# i = 0
# for name in names:
#     print(name)
#     if name == find:
#         print(f'{find} pod indeksem {i}')
#         break
#     i += 1


# names = ['Jan', 'Agata', 'Marcin', 'Dominik', 'Adam']
#
# exclude = 'Agata'
# for name in names:
#     if name == exclude:
#         continue
#     print(name)

# sentence = 'Ala MA koTa oraz pSA.'
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.title())
# print(sentence.replace('Ala', 'Jan'))
#
# print(sentence.count('A'))
# # count numbers of a/A
# print(sentence.lower().count('a'))
# lower_sentence = sentence.lower()
# counter = lower_sentence.count('a')
# print(counter)
#
# count_a = sentence.count('a')
# count_A = sentence.count('A')
# print(count_A + count_a)
#
# words = sentence.split()
# print(words)
# print(' '.join(words))  # join elements into string
#
# for letter in sentence:
#     print(letter)

# # List comprehension
# numbers_list_comprehension = [x for x in range(10)]
#
# numbers_for_loop = []
# for x in range(10):
#     numbers_for_loop.append(x)
#
# print(numbers_for_loop, numbers_list_comprehension)
# print(numbers_list_comprehension == numbers_for_loop)

# List comprehension with if statement
numbers_list_comprehension = [x for x in range(10) if x % 2 == 0]

numbers_for_loop = []
for x in range(10):
    if x % 2 == 0:
        numbers_for_loop.append(x)

print(numbers_for_loop, numbers_list_comprehension)
print(numbers_list_comprehension == numbers_for_loop)
















