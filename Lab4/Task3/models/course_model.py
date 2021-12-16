from Task3.config import db


class CourseModel(db.Model):
    """
    Model for dataTable that represents a Course class
    """
    __tablename__ = 'course'

    def __init__(self, name, course_program):
        self.name = name
        self.course_program = course_program

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    course_program = db.Column(db.String(200), nullable=False)