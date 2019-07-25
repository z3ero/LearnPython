# -*- coding:utf-8 -*-

# 下不修改say原函数代码的情况下增加say的功能，判断age是否符合常理
def say(name, age):
    return "%s is a good man! he is %d years old"%(name, age)
def wrapper(f):
    def inner(name, age):
        #增加功能
        if age <= 0:
            age = 0
        return f(name, age)
    return inner
say = wrapper(say)

print(say("sunck", -18))


