# Python是动态语言
class Person(object):
    count = 0

    # 当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问
    def __init__(self, name, gendar, birth):
        Person.count += 1
        self.name = name
        self.gendar = gendar
        self.birth = birth
        # for k, v in kwargs.items():  # Python 3 renamed dict.iteritems -> dict.items
        #     setattr(self, k, v)


# _xxx 可以在子类中使用。
# __xxx 不可以在子类中使用。
# L1=[a,b,c]
# L2=sorted(L1,key=lambda p:p.name.lower())
# for l in L2:
#     print(l.name)

# p = Person('Xiao Ming', 'Male', '1990-1-1',34, job='Student')
# print(p.job)
# print(p.count)
# print(p.get_grade())
# print(p.__birth)

# 类的继承
class Student(Person):
    def __init__(self, name, gendar, birth, score):
        super(Person, self).__init__(name, gendar, birth)
        self.score = score

    # 成绩分类
    def get_grade(self):
        if self.__score >= 80:
            return 'A'
        if self.__score >= 60:
            return 'B'
        return 'C'

    @classmethod
    def pget_grade(grade):
        return 'A' if grade.__sorce - 80 >= 0 else 'B' if grade.__sorce - 60 >= 0 else 'C'


# Test
s1 = Student("a", "F", "2016", 76)
print(s1.get_grade())
s2 = Student("a", "F", "2016", 45)
print(Student.pget_grade())
