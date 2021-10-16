import string


class Student:
    """
        Class that represent the Student
    """
    __all_id = []
    __all_names = []

    def __init__(self, id, name, surname, age, grades):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades
        pass

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        if value in self.__all_id:
            raise ValueError
        self.__all_id.append(value)
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value:
            raise ValueError
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError
        if value == string.whitespace or not value:
            raise ValueError
        if value+self.__name in self.__all_names:
            raise ValueError
        self.__all_names.append(value+self.__name)
        self.__surname = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError
        if 0 > value < 100:
            raise ValueError
        self.__age = value

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        if not isinstance(value, dict):
            raise TypeError
        if not all(isinstance(key, str) for key in value):
            raise TypeError
        if not all(key == string.whitespace or key for key in value):
            raise ValueError
        if not all(isinstance(item, int) for item in value.values()):
            raise TypeError
        if not all(0 <= item <= 100 for item in value.values()):
            raise ValueError
        self.__grades = value

    def get_average_score(self):
        score = 0
        for value in self.__grades.values():
            score += value
        return score / len(self.__grades)

    def __str__(self):
        return f"{self.__surname} {self.__name} |Age {self.__age} |\nGrades: {self.__grades}"
