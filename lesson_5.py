# classes


class Person:
    first_name = 'Adam'
    last_name = 'Kowalski'
    age = 29
    additional_info = None

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def say_hello(self):
        return f'Hello {self.first_name}'

    @classmethod
    def print_name(cls):
        print(cls.first_name + ' ' + cls.last_name)


# class method
Person.print_name()
Person().print_name()
person_object = Person()
person_object.print_name()

person_object = Person()
print(person_object)
print(person_object.first_name, person_object.last_name, person_object.age, person_object.additional_info)

person_object.first_name = 'Marcin'
print(person_object.first_name)
print(person_object)

print(person_object.say_hello())


class Animal:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        self.additional_info = kwargs.get('additional_info')

    def __str__(self):
        return self.name

    def birthday(self, value=None):
        if value:
            self.age += value
        else:
            self.age += 1

    def hello(self):
        return f'Hello {self.name}, I am an animal.'


animal = Animal('lion', 3)
print(animal, animal.age, animal.additional_info)
monkey = Animal('monkey', 5, additional_info={'number_of_legs': 4})
print(monkey, monkey.age, monkey.additional_info)
monkey.birthday()
monkey.birthday()
print(monkey.age)
monkey.birthday(value=2)
print(monkey.age)


class Lion(Animal):
    def hello(self):
        return f'Hello {self.name}, I am a lion.'


class Monkey(Animal):
    def __init__(self, name, age, bananas, additional_info=None):
        super(Monkey, self).__init__(name, age, additional_info=additional_info)
        self.bananas = bananas

    def hello(self):
        animal_hello = super().hello()  # calls the inherited class method called hello
        return f'{animal_hello} I am a monkey.'

    def eat_banana(self, quantity=None):
        """
        Monkey eats bananas of defined quantity or just one
        :param quantity: amount of bananas to eat
        :return:
        """
        if self.bananas <= 0:
            print('Oh! I am hungry.')
        else:
            print('Yummy!')
            if quantity:
                self.bananas -= quantity
                if self.bananas < 0:
                    self.bananas = 0
            else:
                self.bananas -= 1

    def add_bananas(self, number):
        self.bananas += number

    @property
    def info(self):
        return f'Bananas: {self.bananas}, Additional info: {self.additional_info}'


# multiple inheritance
class MonkeyLionMix(Monkey, Lion):
    pass


mix = MonkeyLionMix('monkey lion', 3, 10)
print(mix)
print(mix.hello())

animal = Animal('random animal', 10)
lion = Lion('lion king', 5)
monkey = Monkey('monkey', 6, 4)

print(animal.hello())
print(lion.hello())
print(monkey.hello())

print(monkey.bananas)
monkey.eat_banana()
monkey.eat_banana()
monkey.eat_banana()
monkey.eat_banana()
monkey.eat_banana()
monkey.eat_banana()
print(monkey.bananas)

monkey.add_bananas(10)

print(monkey.bananas)
monkey.eat_banana()
monkey.eat_banana()
monkey.eat_banana()
monkey.eat_banana()
monkey.eat_banana()
monkey.eat_banana()
print(monkey.bananas)

print(monkey.bananas)
monkey.eat_banana(quantity=7)
print(monkey.bananas)

print(monkey.info)


# abstract classes
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        self.additional_info = kwargs.get('additional_info')

    @abstractmethod
    def hello(self):
        pass

    def birthday(self):
        self.age += 1

    def __str__(self):
        return f'{self.name}'


class Lion(Animal):
    def hello(self):
        return f'Hello. I am {self.name}'


lion = Lion('lion king', 12, additional_info='good lion')
print(lion, lion.name, lion.age, lion.additional_info)
