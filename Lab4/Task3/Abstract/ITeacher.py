from abc import abstractmethod, ABC


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def courses(self):
        raise NotImplementedError