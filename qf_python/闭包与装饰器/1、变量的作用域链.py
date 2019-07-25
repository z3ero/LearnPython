# -*- coding:utf-8 -*-

a = 10
def func1():
    b = 20
    def func2():
        c = 30
        return a + b + c
    return func2()


print(func1())


