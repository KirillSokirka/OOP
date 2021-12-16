from Task3.abstract.icourse_factory import ICourseFactory
from Task3.concrete.course import Course
from Task3.concrete.local_course import LocalCourse
from Task3.concrete.offsite_course import OffsiteCourse


class CourseFactory(ICourseFactory):
    """
    Class that implements ICourseFactory
    """

    @staticmethod
    def create_course(name: str, course_program: str, course_type: str, teacher: list, **kwargs):
        """
        Create course factory method
        :param name: name of course
        :param course_program: course content
        :param course_type: type of course
        :param teacher: list of course teachers
        :param kwargs:
        :return: instance of object that implements ICourse
        """

        if course_type == 'local':
            return LocalCourse(name, course_program, teacher)
        elif course_type == 'offset':
            return OffsiteCourse(name, course_program, teacher)
        else:
            return Course(name, course_program, teacher)