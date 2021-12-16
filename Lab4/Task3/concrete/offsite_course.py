from Task3.concrete.course import Course
from Task3.abstract.ioffsite_course import IOffsiteCourse


class OffsiteCourse(Course, IOffsiteCourse):
    """
    Class for offsite course
    Extends Course
    Implements IOffSiteCourse
    """

    def __init__(self, name, program, teacher):
        super().__init__(name, program, teacher)

    def study(self):
        """
            Imitate studying offset
            :return: silly string message
        """
        return  'Studying offsite'

    def __str__(self) -> str:
        return super().__str__() + \
               f'\n\tGoes offset'
