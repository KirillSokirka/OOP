from abc import abstractmethod

from Task3.Abstract.ICourse import ICourse


class ILocalCourse(ICourse):

    @abstractmethod
    def study(self):
        raise NotImplementedError
