# ThreadLock: 每个线程独立的存储空间
import threading

local = threading.local()
lock = threading.Lock()
money = 0
def changeMoney(x, n):
    x += n
    x -= n

def run1(num):
    local.money = num
    for i in range(3):
        with lock:
            print('run1 ----', local.money)

def run2(num):
    local.money = num
    for i in range(3):
        with lock:
            print('run2------', local.money)
th1 = threading.Thread(target=run1, args=(1,))
th2 = threading.Thread(target=run2, args=(2,))
th1.start()
th2.start()
th1.join()
th1.join()

