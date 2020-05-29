# Errors continue

result = None
print('Enter to valid integers and enter after each one')
first_number = input()
second_number = input()

try:
    result = int(first_number) / int(second_number)
except ZeroDivisionError:
    print('You cannot divide a number by 0')
except ValueError:
    print('Input valid number')


print(result)


class InvalidGender(Exception):
    pass


from homework_5 import Worker
from constants.users import GenderChoices  # from module constants.users imports class GenderChoices
# import constants  # imports module constants
# from constants.users import *  # from module constants.users import everything, try to avoid


class EnhancedWorker(Worker):
    def __init__(self, first_name, last_name, salary, level, gender):
        super().__init__(first_name, last_name, salary, level, gender)
        if self.gender not in GenderChoices.choices():
            raise InvalidGender('Invalid gender: choose one from: male, female')
        try:
            self.level = int(self.level)
        except ValueError:
            print('Level should be an integer')
            raise


# # Throws errors
# worker = EnhancedWorker('Marysia', 'Kowalska', 5000, 'test_level', 'male')
# print(worker)

# worker = EnhancedWorker('Marysia', 'Kowalska', 5000, 1, 'unknown')
# print(worker)

worker = Worker('Marysia', 'Kowalska', 5000, 1, 'male')
print(worker)
