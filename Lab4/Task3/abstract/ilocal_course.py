from abc import abstractmethod

from Task3.abstract.icourse import ICourse


class ILocalCourse(ICourse):
    """
    Interface for local courses
    extend interface ICourse

    Methods
    -------
    study()
        abs method
    """

    @abstractmethod
    def study(self):
        raise NotImplementedError
