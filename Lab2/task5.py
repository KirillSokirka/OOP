from Classes.Student import Student
from Classes.Group import Group


def main():
    petya = Student(1, "Pupkin", "Petya", 18, {
        "Math" : 60,
        "Sceince" : 90,
        "Art" : 80
    })
    john = Student(2, "Smith", "John", 18, {
        "Math": 65,
        "Sceince": 80,
        "Art": 70
    })
    alex = Student(3, "Brown", "Alex", 18, {
        "Math" : 100,
        "Sceince" : 100,
        "Art" : 60
    })
    peter = Student(5, "Parker", "Peter", 18, {
        "Math" : 99,
        "Sceince" : 100,
        "Art" : 95
    })
    bob = Student(6, "Davis", "Bob", 18, {
        "Math": 99,
        "Sceince": 100,
        "Art": 95
    })
    group = Group(3, petya, peter, alex, john)
    group.add_student(bob)
    print(group.find_top_five())
    print(group.find_average())


main()
