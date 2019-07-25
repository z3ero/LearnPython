# -*- coding:utf-8 -*-
def wrapper1(f):
    print("enter wrapper1")
    def inner1(*args, **kwargs):
        print("enter inner1")
        res = f(*args, **kwargs)
        print("exit inner1")
        return res
    print("exit wrapper1")
    return inner1

def wrapper2(f):
    print("enter wrapper2")
    def inner2(*args, **kwargs):
        print("enter inner2")
        res = f(*args, **kwargs)
        print("exit inner2")
        return res
    print("exit wrapper2")
    return inner2

def wrapper3(f):
    print("enter wrapper3")
    def inner3(*args, **kwargs):
        print("enter inner3")
        res = f(*args, **kwargs)
        print("exit inner3")
        return res
    print("exit wrapper3")
    return inner3

'''
装饰时：从距离近的装饰器开始装饰
执行时：从距离远的装饰器内部函数开始执行
'''
@wrapper1
@wrapper2
@wrapper3
def func(x, y):
    return x + y

print("----------------")
func(1, 2)



'''
inner3 = wrapper3(func)
inner2 = wrapper2(inner3)
inner1 = wrapper1(inner2)
func = inner1
'''
