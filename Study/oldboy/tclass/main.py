# Object Oriented Programming
from oldboy.tclass import person, student

if __name__ == "__main__":
    p1 = person.Person("leal", "M", 23)
    p1.showCount()
    p2 = person.Person("lidan", "F", 23)
    p3 = person.Person("we", "F", 23)
    p1.showMsg()
    s1 = student.Student("leal", "M", 23, 100)
    s2 = student.Student("lidan", "F", 23, 121)
    print(s1.score)
    # print(type(s1))
    # print(dir(s1))
    s1.showMsg()
    print(s1 == s2)
    print(s1 + s2)
