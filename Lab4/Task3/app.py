from Task3.Concrete.CourseFactory import CourseFactory
from Task3.Concrete.Teacher import Teacher
from Task3.Repos.DbCoursesRepo import DbCoursesRepo


if __name__ == '__main__':
    t = Teacher('david')
    #DbManager.add_teacher(t)
#    c = CourseFactory.create_course('Python for beginners', ['Print', 'List', 'Tuple'], 'offset', t, )
    f = CourseFactory.create_course('Python for not beginners', 'SQL, Flask', 'offset', [t])
    d = CourseFactory.create_course('Python for master', 'Ai, UI, IU', 'local', [t])
    # DbManager.add_courses_to_teacher([f], t.name)
    #DbManager.add_courses_to_teacher([c], t.name)
    DbCoursesRepo.add_course(d, t)
    res = DbCoursesRepo.get_course_by_name('Python for master')
    print(t)
