from Task3.Abstract import ITeacher
from Task3.Abstract.ICourseFactory import ICourseFactory
from Task3.Concrete.Course import Course
from Task3.Concrete.LocalCourse import LocalCourse
from Task3.Concrete.OffsiteCourse import OffsiteCourse


class CourseFactory(ICourseFactory):

    @staticmethod
    def create_course(name: str, course_program: str, course_type: str, teacher: list, **kwargs):
        if course_type == 'local':
            return LocalCourse(name, course_program, teacher)
        elif course_type == 'offset':
            return OffsiteCourse(name, course_program, teacher)
        else:
            return Course(name, course_program, teacher)