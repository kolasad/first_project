from enum import Enum


class GenderChoices(Enum):
    MALE = 'male'
    FEMALE = 'female'

    @classmethod
    def choices(cls):
        return [choice.value for choice in cls]
