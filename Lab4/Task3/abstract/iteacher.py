from abc import abstractmethod, ABC


class ITeacher(ABC):
    """
        Interface for local courses
        extend interface ICourse

        Properties:

            name:
                abstract property of teacher name
            courses:
                abstract property for teacher courses
        """

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def courses(self):
        raise NotImplementedError