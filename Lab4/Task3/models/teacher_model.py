from Task3.config import db

"""
Additional table for impelementing many-to
"""
teacher_courses = db.Table(
    'teacher_courses',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True),
    db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'), primary_key=True)
)


class TeacherModel(db.Model):
    """
        Model for dataTable that represents a Teacher class
    """
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    courses = db.relationship('CourseModel', secondary=teacher_courses,
                              lazy='subquery',
                              backref=db.backref('teachers'))

