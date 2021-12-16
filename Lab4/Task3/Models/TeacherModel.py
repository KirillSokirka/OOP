from Task3.Config import db


teacher_courses = db.Table(
    'teacher_courses',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True),
    db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'), primary_key=True)
)


class TeacherModel(db.Model):
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    courses = db.relationship('CourseModel', secondary=teacher_courses,
                              lazy='subquery',
                              backref=db.backref('teachers'))

