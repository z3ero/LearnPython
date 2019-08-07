# 多线程共享数据： 容易造成变量值不能正确操作
import threading

money = 0
def changeMoney(n):
    global money
    money += n
    money -= n

def run1(num):
    for i in range(100000):
        changeMoney(num)

def run2(num):
    for i in range(100000):
        changeMoney(num)

th1 = threading.Thread(target=run1, args=(5,))
th2 = threading.Thread(target=run1, args=(8,))
th1.start()
th2.start()
th1.join()
th1.join()
print(money)


