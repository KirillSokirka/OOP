from abc import abstractmethod, ABC


class ICourse(ABC):

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