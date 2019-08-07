class TestMinXin(object):
    def func1(self):
        pass
    def say(self):
        print("i am mixin")

class Person(object):
    def say(self):
        print("i am a person")

class Student(Person):
    pass

stu = Student()
stu.say()

def mixin(pyClass, pyMixinClass, flag=0):
    if flag:  # flag 为1， 表示将mixin类设置为主 父类
        pyClass.__bases__ = (pyMixinClass,) + pyClass.__bases__
    elif pyMixinClass not in pyClass.__bases__:
        pyClass.__bases__ += (pyMixinClass,)
    else:
        pass

mixin(Student, TestMinXin, 1)
print(Student.mro())
stu.say()