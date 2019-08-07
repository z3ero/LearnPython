# 多线程任务时，各个线程的执行顺序是不确定的
# 线程调度——让线程按照一定的顺序运行
# 任务1: 两个线程分别打印 0-9内的奇数和偶数，要求打印顺序按照 0，1，2，3，4，5，6，7，8，9
# 线程条件变量
import threading
cond = threading.Condition()

def run1():
    with cond:
        for i in range(0,10,2):
            print("run1---", i)
            cond.wait()
            cond.notify()

def run2():
    with cond:
        for i in range(1,10,2):
            print("run2---", i)
            cond.notify()
            cond.wait()


th1 = threading.Thread(target=run1)
th2 = threading.Thread(target=run2)
th1.start()
th2.start()
th1.join()
th2.join()
