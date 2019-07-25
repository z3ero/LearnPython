# -*- coding:utf-8 -*-

def retry(count=3, wait=0,exceptions=(Exception,)):
    import time
    def wrapper(f):
        def inner(*args, **kwargs):
            for i in range(count):
                try:
                    print("-------------------")
                    res = f(*args, **kwargs)
                except exceptions as e:
                    time.sleep(wait)
                    continue
                else:
                    return res
        return inner
    return wrapper

import random

@retry(5)
def connetSQL(ip, port, dbName, passwd):
    num = random.choice([1,2,3,4])
    print("**************", num)
    if num <= 4:
        10 / 0

connetSQL("", "", "", "")
