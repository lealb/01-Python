class Person(object):
    perCount = 0

    # 魔术方法 继承 __new__
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception("Age Must Int")

        Person.perCount += 1

    def showCount(self):
        print("Total Person %d" % Person.perCount)

    def showMsg(self):
        print("Name : ", self.name, ", Gender: ", self.gender, ", Age: ", self.age)
