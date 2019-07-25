#  7.15 修饰器的缺点:
#  1. 不支持关键字参数
#  2. 遮盖了被修饰函数的 __name__ 和 __doc__ 属性
#  下面使用 functiontools.wraps 装饰器
#  (1) 相关的属性从 func 复制到clocked中
#  (2) 正确处理关键字参数

import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s = %r'%(k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs]%s(%s) -> %r'%(t, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds, **kwargs):
    time.sleep(seconds)
    return 'sleep %d'%seconds

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__=="__main__":
    print('*'*40, 'Calling snooze(.900)')

    # 让装饰器可以处理 kwargs 参数
    d = {'a': 'aaa', 'b': 'bbb'}
    snooze(.900, **d)
    print('*'*40, 'Calling factorial(6)')
    print('6!=', factorial(6))
