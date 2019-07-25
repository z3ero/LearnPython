# -*- coding:utf-8 -*-

def count(f):
    index = 0
    def inner(*args, **kwargs):
        nonlocal index
        index += 1
        res = f(*args, **kwargs)
        print("第%d次执行"%index)
        return res
    return inner

@count
def func():
    print("sunck is a good man")


@count
def func1():
    print("sunck is a nice man")

func()
func()
func1()
func()
func1()

