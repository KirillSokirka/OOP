from Task3.Concrete.Course import Course
from Task3.Abstract.ILocalCourse import ILocalCourse


class LocalCourse(Course, ILocalCourse):

    def __init__(self, name, program, teacher):
        super(Course, self).__init__(name, program, teacher)

    def study(self):
        print('Studying locally')

    def __str__(self) -> str:
        return super().__str__() + \
               f'\n\tGoes locally'