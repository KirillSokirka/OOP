from Task3.config import db
from Task3.models.course_model import CourseModel
from Task3.abstract.icourse import ICourse
from Task3.abstract.iteacher import ITeacher
from Task3.models.teacher_model import TeacherModel, teacher_courses


class DbTeacherRepo:

    @staticmethod
    def add_teacher(teacher: ITeacher):
        """
        Adds teacher to db
        """
        tempT = TeacherModel.query.filter_by(name=teacher.name).first()
        if tempT:
            return
        tempT = TeacherModel()
        tempT.name = teacher.name
        if len(teacher.courses) != 0:
            for course in teacher.courses:
                tempT.courses.append(CourseModel(course.name, course.course_program))
        db.session.add(tempT)
        db.session.commit()

    @staticmethod
    def add_courses_to_teacher(courses : [], teacher_name):
        """
        Adds courses to teacher
        :param courses: new courses
        :param teacher_name: name of teaher
        :raise ValueError if teacher doesn't exists
        """
        teacher = db.session.query(TeacherModel).filter_by(name=teacher_name).first()
        if not teacher:
            raise ValueError
        for course in courses:
            teacher.courses.append(CourseModel(course.name, course.course_program))
        db.session.commit()

    @staticmethod
    def get_all_teacher_courses(teacher: ITeacher):
        """
        Method for getting all teachers courses
        :param teacher: teacher that courses we want
        :return: list of courses
        """
        list_of_models = CourseModel.query \
            .filter(CourseModel.teachers.any(name=teacher.name)).first()
        list_of_courses = []
        for model in list_of_models:
            from Task3.concrete.course import Course
            list_of_courses.append(Course(model.name, model.course_program, teacher))
        return list_of_courses