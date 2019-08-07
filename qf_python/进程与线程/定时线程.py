import time
import threading

def fun():
    print("thread running")

if __name__=="__main__":
    # 在主机进程启动5秒后再执行，不会阻塞主线程
    th = threading.Timer(5, fun)
    th.start()
    th.join()


