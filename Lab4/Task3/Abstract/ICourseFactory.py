from abc import abstractmethod, ABC

from Task3.Abstract import ITeacher


class ICourseFactory(ABC):

    @staticmethod
    @abstractmethod
    def create_course(name: str, course_program: str, course_type: str, teacher: list):
        raise NotImplementedError
