# 多线程共享数据： 容易造成变量值不能正确操作
import threading

lock = threading.Lock()
money = 0
def changeMoney(n):
    global money
    money += n
    money -= n

def run1(num):
    global lock
    for i in range(100000):
        lock.acquire()
        try:
            changeMoney(num)
        finally:
            lock.release()
def run2(num):
    global lock
    for i in range(100000):
        lock.acquire()
        try:
            changeMoney(num)
        finally:
            lock.release()
'''
上述用锁，用 with lock: 其实更好，自动加锁，放锁
'''
th1 = threading.Thread(target=run1, args=(5,))
th2 = threading.Thread(target=run1, args=(8,))
th1.start()
th2.start()
th1.join()
th1.join()
print(money)


