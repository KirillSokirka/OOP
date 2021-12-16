from abc import abstractmethod, ABC


class IOffsiteCourse(ABC):
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
