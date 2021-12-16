from abc import abstractmethod, ABC


class ICourseFactory(ABC):
    """
    Interface for course factory

    """
    @staticmethod
    @abstractmethod
    def create_course(name: str, course_program: str, course_type: str, teacher: list):
        raise NotImplementedError
