from Task3.Abstract.ICourse import ICourse
from Task3.Abstract.ITeacher import ITeacher
from Task3.Concrete.Teacher import Teacher


class Course(ICourse):

    def __init__(self, name, course_program, teacher):
        self.name = name
        self.course_program = course_program
        self.teacher = teacher

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
    def course_program(self):
        return self.__course_program

    @course_program.setter
    def course_program(self, value):
        if not isinstance(value, str):
            raise ValueError
        self.__course_program = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, list):
            raise TypeError
        if not all(isinstance(teacher, ITeacher) for teacher in value):
            raise TypeError
        self.__teacher = value

    def __str__(self) -> str:
        return f'Course:' \
               f'\n\tname - {self.__name}' \
               f'\n\tteacher - {" ".join(self.__teacher)}' \
               f'\n\tprogram - {self.__course_program}'
