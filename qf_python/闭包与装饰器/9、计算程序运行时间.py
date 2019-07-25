# -*- coding:utf-8 -*-
import time

def timer(f):
    def inner(*args, **kwargs):
        time1 = time.time()
        res = f()
        time2 = time.time()
        print("程序运行:%f"%(time2-time1))
        return res
    return inner

@timer
def func():
    print("sunck is a nice man")
    time.sleep(2)
    print("sunck is a good man")

func()



