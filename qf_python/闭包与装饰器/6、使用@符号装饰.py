# -*- coding:utf-8 -*-
'''
python2.4支持使用@将装饰器应用在函数上，只需要再函数定义前加上@装饰器的名称即可

'''
def wrapper(f):
    def inner(name, age):
        #增加功能
        if age <= 0:
            age = 0
        return f(name, age)
    return inner

@wrapper
def say(name, age):
    return "%s is a good man! he is %d years old"%(name, age)

# 相当于  say = wrapper(say)

print(say("sunck", -18))


