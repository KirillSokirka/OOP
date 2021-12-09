from Task3.Abstract import ITeacher


from abc import ABC, abstractmethod


class ICourseFactory(ABC):

    @abstractmethod
    def create_course(self, name: str, course_program: list, course_type: str ,teacher : ITeacher):
        raise NotImplementedError