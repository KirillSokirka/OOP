from Task3.Abstract.ICourse import ICourse
from Task3.Abstract.ITeacher import ITeacher


class Teacher(ITeacher):

    def __init__(self, name, courses=None):
        self.name = name
        if courses:
            self.courses = courses
        else:
            self.__courses = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value.rstrip():
            raise ValueError
        self.__name = value

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        if not isinstance(value, list):
            raise TypeError
        if not all(isinstance(c, ICourse) for c in value):
            raise ValueError
        self.__courses = value

    def __str__(self):
        return f'Teacher:' \
               f'\n\tname - {self.__name}'\
               f'\n\tcourses - {",".join(x.name for x in self.__courses)}'


