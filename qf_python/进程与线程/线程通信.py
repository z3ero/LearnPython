# 线程信号
import time
import threading

def func():
    event = threading.Event()   # 创建线程事件对象
    def run():
        for i in range(10):
            # 阻塞
            event.wait()
            # 重置信号
            event.clear()
            print("----"+str(i))
    th = threading.Thread(target=run)
    th.start()
    return event

# 主线程通过信号控制子线程运行
event = func()
for i in range(10):
    event.set()
    time.sleep(1)
