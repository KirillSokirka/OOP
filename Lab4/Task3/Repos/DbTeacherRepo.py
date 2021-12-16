from Task3.Config import db
from Task3.Models.CourseModel import CourseModel
from Task3.Abstract.ICourse import ICourse
from Task3.Abstract.ITeacher import ITeacher
from Task3.Models.TeacherModel import TeacherModel, teacher_courses


class DbTeacherRepo:

    @staticmethod
    def add_teacher(teacher: ITeacher):
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
        teacher = db.session.query(TeacherModel).filter_by(name=teacher_name).first()
        if not teacher:
            raise ValueError
        for course in courses:
            teacher.courses.append(CourseModel(course.name, course.course_program))
        db.session.commit()

    @staticmethod
    def get_all_teacher_courses(teacher: ITeacher):
        list_of_models = CourseModel.query \
            .filter(CourseModel.teachers.any(name=teacher.name)).first()
        list_of_courses = []
        for model in list_of_models:
            from Task3.Concrete.Course import Course
            list_of_courses.append(Course(model.name, model.course_program, teacher))
        return list_of_courses