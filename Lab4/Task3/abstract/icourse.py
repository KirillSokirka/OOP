from abc import abstractmethod, ABC


class ICourse(ABC):
    """
    Interface for course

    Properties:
        name:
            abstract property for course name
        teacher:
            abstract property for teacher name
        course_program:
            abstract property for course content
    """

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def teacher(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def course_program(self):
        raise NotImplementedError
