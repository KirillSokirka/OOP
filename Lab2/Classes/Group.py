from Student import Student

class Group:

    __count_of_students = 0
    __all_id = []

    def __new__(cls, id, *args):
        if Group.__count_of_students > 20:
            raise Exception("Too many students")
        return super(Group, cls).__new__(cls)

    def __init__(self, id, *args):
        self.id = id
        self.__students = Group.__validate(list(args))
        Group.__count_of_students += 1

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        if value in self.__all_id:
            raise ValueError
        self.__all_id.append(value)
        self.__id = value

    @property
    def students(self):
        return self.__students

    @staticmethod
    def __validate(value):
        if not isinstance(value, list):
            raise TypeError
        if not all(isinstance(item, Student) for item in value):
            raise TypeError
        if not all(value.count(student) == 1 for student in value):
            raise ValueError
        return value

    def add_student(self, student):
        if Group.__count_of_students > 20:
            raise Exception("Too mane students")
        if not isinstance(student, Student):
            raise TypeError
        if student in self.__students:
            raise ValueError
        self.__students.append(student)
        Group.__count_of_students += 1

    def del_student(self, id):
        if not isinstance(id, int):
            raise ValueError
        for student in self.students:
            if student.id == id:
                self.__students.remove(student)
                Group.__count_of_students -= 1
                break

    def find_average(self) -> dict:
        temp = {}
        for student in self.__students:
            temp[student.name] = student.get_average_score()
        return temp

    def find_top_five(self):
        top_students = self.find_average()
        top_students = {key: value for key, value in
                        sorted(top_students.items(), key=lambda item: item[1], reverse=True)}
        if len(top_students) < 5:
            return list(top_students.items())[0]
        return list(top_students.items())[0:5]
