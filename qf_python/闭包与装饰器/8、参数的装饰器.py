# -*- coding:utf-8 -*-

def wrapper(count=3):
    def deco(f):
        def inner(*args, **kwargs):
            for i in range(count):
                f(*args, **kwargs)
        return inner
    return deco

@wrapper()
def func():
    print("sunck is a good man")

func()




