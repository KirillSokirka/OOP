from Task3.Concrete.Course import Course
from Task3.Concrete.Teacher import Teacher
from Task3.Config import db
from Task3.Models.CourseModel import CourseModel
from Task3.Abstract.ICourse import ICourse
from Task3.Abstract.ITeacher import ITeacher
from Task3.Models.TeacherModel import TeacherModel


class DbCoursesRepo:

    @staticmethod
    def get_courses():
        return CourseModel.query.all()

    @staticmethod
    def add_course(course: ICourse, teacher: ITeacher):
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
        temp = CourseModel.query.filter_by(name=name).first()
        teacher_list = []
        for teacher in temp.teachers:
            teacher_list.append(Teacher(teacher.name))
        return Course(temp.name, temp.course_program, teacher_list)



