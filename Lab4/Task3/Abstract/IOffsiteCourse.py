from abc import abstractmethod, ABC


class IOffsiteCourse(ABC):

    @abstractmethod
    def study(self):
        raise NotImplementedError
