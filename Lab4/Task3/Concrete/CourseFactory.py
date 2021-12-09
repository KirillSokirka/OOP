from Task3.Abstract import ITeacher
from Task3.Abstract.ICourseFactory import ICourseFactory
from Task3.Concrete.LocalCourse import LocalCourse
from Task3.Concrete.OffsiteCourse import OffsiteCourse


class CourseFactory(ICourseFactory):

    def create_course(self, name: str, course_program: list, course_type: str, teacher: ITeacher):
        if course_type == 'local':
            return LocalCourse(name, course_program, teacher)
        elif course_type == 'offset':
            return OffsiteCourse(name, course_program, teacher)
