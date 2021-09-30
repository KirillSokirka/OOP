import sys


class Student:
    surnames = []

    def __new__(cls, **kwargs):
        surname = kwargs["surname"]
        if surname in Student.surnames:
            return None
        return super(Student, cls).__new__(cls)

    def __init__(self, **kwargs):
            for key in kwargs:
                self.__dict__[key] = kwargs[key]
            Student.surnames.append(kwargs["surname"])

    def __str__(self):
        return ", ".join(map(str, self.__dict__.items()))


def main():
    petya = Student(name="Petya", surname="Pupkin", weight=5)
    print(type(petya))
    petya1 = Student(name="Petya", surname="Pupkin", weight=5)
    print(type(petya1))


main()
