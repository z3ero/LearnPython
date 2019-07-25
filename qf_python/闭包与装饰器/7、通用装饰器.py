# -*- coding:utf-8 -*-

def wrapper(f):
    def inner(*args, **kwargs):
        #在这增加功能
        print("no zuo no die")
        res = f(*args, **kwargs)
        #如果要修改原函数的返回值，在这修改
        return res
    return inner



@wrapper
def func(name, age):
    print(name, age)
    return "sunck is a good man"

print(func("kaige", 17))

@wrapper
def func2(height):
    print(height)
    print("**********")
func2(111)