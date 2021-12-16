from Task3.abstract.icourse import ICourse
from Task3.abstract.iteacher import ITeacher


class Course(ICourse):
    """
    Class that represents course entity
    Implements interface ICourse
    """

    def __init__(self, name, course_program, teacher):
        """
        init method for this class
        :param name: course name
        :param course_program: content that will be in the course
        :param teacher: course teachers
        """
        self.name = name
        self.course_program = course_program
        self.teacher = teacher

    @property
    def name(self):
        """
        getter for self.__name
        :return: name of course
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        setter for self.__value
        :param value: a value for name field
        :raise TypeError when type is not str
        :raise ValueError when value is empty
        """
        if not isinstance(value, str):
            raise TypeError
        if not value.rstrip():
            raise ValueError
        self.__name = value

    @property
    def course_program(self):
        """
         getter for self.__course_program
        :return: self.__course program
        """
        return self.__course_program

    @course_program.setter
    def course_program(self, value):
        """
        :raise ValueError when value is not str
        :param value:
        :raise ValueError when value is not str
        """
        if not isinstance(value, str):
            raise ValueError
        self.__course_program = value

    @property
    def teacher(self):
        """
        getter for self.__teacher field
        :return: self.__teacher
        """
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        """
        Teachers of the course setter
        :param value: a new list of Teachers
        :raise TypeError when value type isn't a list
        :raise TypeError when value list contains not ITeacher objects
        """
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
