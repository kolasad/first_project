# 1
# Write a class representing a 2D point: Point2D. Constructor should have two arguments x, y
# define a __str__ method for that class
# write a method calculating a distance between two points
import math


class Point2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'2D point, x={self.x}, y={self.y}'

    def calculate_distance(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def calculate_distance_coordinates(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)


point = Point2D(1, 2)
print(point)
point2 = Point2D(1, 3)
print(point2)

distance = point.calculate_distance(point2)
print(distance)

distance = point.calculate_distance_coordinates(2, 5)
print(distance)

# 2
# Write a class which inherits from Print2D class and implements 3D point, the arguments should be x, y, z
# write a __str__ method for that class (you can use super)
# write a method calculating a distance between two points


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f'3D point, x={self.x}, y={self.y}, z={self.z}'

    def calculate_distance(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2 + (self.z - point.z)**2)


# point_3d = Point3D(1, 1, 1)
# print(point_3d)
# second_point_3d = Point3D(2, 2, 2)
# print(point_3d.calculate_distance(second_point_3d))

# 3
# Write a Worker class which will take first_name, last_name, salary, level and gender
# write a __str__ and __init__ methods. Add method to level up and a method to increase salary by some value or
# percentage
# use inheritance and write a Manager, DataAnalytics, Programmer and SeniorProgrammer
# write a method in Manager class to set salary for others
# write a method do_programming for programmers which will return some HTML code in string
# write a method which will return some data in a list od dictionaries for data scientist


class Worker:
    def __init__(self, first_name, last_name, salary, level, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.level = level
        self.gender = gender

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def increase_salary(self, amount=None, percentage=None):
        if amount:
            self.salary += amount  # self.salary = self.salary + amount
        elif percentage:
            self.salary += (self.salary * percentage / 100)

    def level_up(self):
        self.level += 1
        self.increase_salary(percentage=5)


class DataAnalytics(Worker):
    @staticmethod
    def get_data():
        return [
            {
                'id': 1,
                'name': 'T-shirt',
                'price': 20.60
            },
            {
                'id': 2,
                'name': 'Dress',
                'price': 10.40
            }
        ]


# worker = Worker('Marysia', 'Kowalska', 5000, 1, 'female')
# analyt = DataAnalytics('Marcin', 'Kowalski', 6000, 2, 'male')
#
# print(worker)
# print(analyt)
#
# print(worker.salary)
# worker.increase_salary(amount=200)
# print(worker.salary)
# print(worker.level, worker.salary)
# worker.level_up()
# print(worker.level, worker.salary)
#
# print(analyt.get_data())
