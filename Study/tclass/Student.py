from tcass import Person


class Student(Person):
    def __init__(self, name, sex, age, score):
        super(Person, self).__init__(name, sex, age, score)
        self.score = score
