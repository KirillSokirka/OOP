from Task3.concrete.course import Course
from Task3.abstract.ilocal_course import ILocalCourse


class LocalCourse(Course, ILocalCourse):
    """
    Class for local course
    Extends Course
    Implements ILocalCourse
    """

    def __init__(self, name, program, teacher):
        super().__init__(name, program, teacher)

    def study(self):
        """
        Imitate studying locally
        :return: silly string message
        """
        return 'Studying locally'

    def __str__(self) -> str:
        return super().__str__() + \
               f'\n\tGoes locally'
