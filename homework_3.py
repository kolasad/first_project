# 1
# Write a program which takes input from user until the user enters a number greater or equal than 10
# If valid number is written it's printed to console
#

# while True:
#     number = float(input())
#     if number >= 10:
#         print(number)
#         break
#     else:
#         print('Please select value greater or equal to 10')


# 2 write a program where user enter the car speed and a boolean value - True if it's user birthday,
# False if not
# program should print the ticket value for each speed:
# if speed is less than 50 print to console: 'No ticket'
# if speed is between 50 and 80 print to console: 'Medium ticket'
# if speed is greater than 80 print to console: 'Highest ticket'
# when it's users birthday speed limits increase by 5

# print('Enter speed:')
# speed = float(input())
# print('Enter birthday:')
# is_birthday = input()
# if is_birthday in ['True', 'true', '1']:
#     speed -= 5
# if speed < 50:
#     print('No ticket')
# elif 80 > speed > 50:
#     print('Medium ticket')
# else:
#     print('Highest ticket')

# 3. a write a program that will add all numbers from 0 to 1000 which are divided by the
# number given by user, the list should be printed in console
# 3. b use list comprehension

# a
# number = float(input())
# numbers = []
# for x in range(1001):
#     if x % number == 0:
#         numbers.append(x)
# print(numbers)

# b
# number = float(input())
# print([x for x in range(1001) if x % number == 0])

# 4 a Write a program which will print 10 random integers from 0 to 10
# 4 b put them into a list and print to console
# 4 c use list comprehension and print to console
# 4 d select max, min, median and average value from those numbers

import random

# a
for x in range(10):
    print(random.randint(0, 10))

# b
numbers = list()
for x in range(10):
    numbers.append(random.randint(0, 10))
print(numbers)

# c
numbers = [random.randint(0, 10) for x in range(10)]
print(numbers)

# d
print(max(numbers))
print(min(numbers))

from statistics import median

print(median(numbers))
print(sum(numbers)/len(numbers))
