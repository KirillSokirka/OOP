from Task3.concrete.course import Course
from Task3.concrete.teacher import Teacher
from Task3.config import db
from Task3.models.course_model import CourseModel
from Task3.abstract.icourse import ICourse
from Task3.abstract.iteacher import ITeacher
from Task3.models.teacher_model import TeacherModel


class DbCoursesRepo:
    """
    class that working with db
    """

    @staticmethod
    def get_courses():
        """
        Method for getting all courses
        :return: all available courses
        """
        return CourseModel.query.all()

    @staticmethod
    def add_course(course: ICourse, teacher: ITeacher):
        """
        Adding course to datatable
        :param course: course
        :param teacher: Teacher
        :raise TypeError if course is not ICourse
        :raise TypeError if course is not ITeacher
        """
        if not isinstance(course, ICourse):
            raise TypeError
        if not isinstance(teacher, ITeacher):
            raise TypeError
        t = db.session.query(TeacherModel).filter_by(name=teacher.name).first()
        if not t:
            raise ValueError
        c = CourseModel(course.name, course.course_program)
        t.courses.append(c)
        db.session.commit()

    @staticmethod
    def get_course_by_name(name) -> ICourse:
        """
        Get course by it name
        :param name: name of course
        :return: None if this course doesn't exists or Course
        """
        temp = CourseModel.query.filter_by(name=name).first()
        if not temp:
            return None
        teacher_list = []
        for teacher in temp.teachers:
            teacher_list.append(Teacher(teacher.name))
        return Course(temp.name, temp.course_program, teacher_list)



