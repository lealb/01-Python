from tclass import person


class Student(person.Person):
    def __init__(self, name, gender, age, score):
        super(Student, self).__init__(name, gender, age)
        self.score = score

    def showMsg(self):
        print("Name : ", self.name, ", Gender: ", self.gender, ", Age: ", self.age, ", Score: ", self.score)

    def showCount(self):
        super().showCount()

    def __str__(self) -> str:
        return super().__str__()

    def __eq__(self, other):
        if isinstance(self, Student):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception("Unknown Object")

    def __add__(self, other):
        if isinstance(self, Student):
            return self.age + self.age
        else:
            raise Exception("Unknown Object")
