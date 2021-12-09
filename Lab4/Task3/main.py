from Task3.Concrete.CourseFactory import CourseFactory
from Task3.Concrete.Teacher import Teacher

if __name__ == '__main__':
    t = Teacher('David')
    factory = CourseFactory()
    c = factory.create_course('Python for beginers', ['Print', 'List', 'Tuple'], 'offset', t)
    c.study()
    print(t)
    print(factory)