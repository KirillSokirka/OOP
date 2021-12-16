from Task3.Concrete.Course import Course
from Task3.Abstract.IOffsiteCourse import IOffsiteCourse


class OffsiteCourse(Course, IOffsiteCourse):

    def __init__(self, name, program, teacher):
        super().__init__(name, program, teacher)

    def study(self):
        print('Studying offsite')

    def __str__(self) -> str:
        return super().__str__() + \
               f'\n\tGoes offset'
