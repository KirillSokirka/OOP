from abc import abstractmethod, ABC


class ILocalCourse(ABC):

    @abstractmethod
    def study(self):
        raise NotImplementedError
