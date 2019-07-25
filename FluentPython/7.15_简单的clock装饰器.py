import time
# 一个简单修饰器，输出函数运行时间
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        t = time.perf_counter()-t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs]%s(%s) -> %r'%(t, name, arg_str, result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)
    return 'sleep %d'%seconds

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__=="__main__":
    print('*'*40, 'Calling snooze(.900)')
    snooze(.900)
    print('*'*40, 'Calling factorial(6)')
    print('6!=', factorial(6))


'''
工作原理

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
    
等价于如下代码
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
    
factorial = clock(factorial)
'''
