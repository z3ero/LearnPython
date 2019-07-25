# -*- coding:utf-8 -*-


'''闭包
概念：在函数体中定义内部函数，并且使用了外部函数的变量，然后把内部函数给返回，那么这个内部函数就是闭包

优点：避免污染全局环境，这样就可以在函数体外使用函数体中定义的变量

缺点：数据长期驻留在内存中，造成内存极大的浪费。


'''
a = 10
def func1():
    b = 20
    def func2():
        c = 30
        return a
    return func2


f2 = func1()
print(f2())





def func3():
    b = 40
    def func4():
        return b
    return func4






