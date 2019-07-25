# -*- coding:utf-8 -*-

def func():
    print("sunck is a good man")

def wrapper(f):
    def inner():
        print("***********")
        f()
    return inner

# d = wrapper(func)
# d()
func = wrapper(func)
func()





