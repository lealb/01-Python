import tcass


class Student(Person):
    def __init__(self, name, sex, age):
        super(Person, self).__init__(name, sex, age, score)
        self.score = score
