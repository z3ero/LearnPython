# 在 IO 密集型 的网络编程中，异步处理比同步处理 性能更高 2个量级以上

# 同步： 阻塞一直等待，不阻塞再继续完成任务
# 异步： 阻塞不等待，去干别的，不阻塞通知我，回来继续完成任务


# 同步代码: 阻塞运行
import time

def func():
    time.sleep(1)
    print('time: %s'%time.time())

for i in range(5):
    func()


# 异步代码： 非阻塞运行，几乎同时运行
import asyncio

# 定义异步函数 (就是一个协程)
async def func():
    # 模拟一个耗时的IO操作，但是不会阻塞
    asyncio.sleep(1)
    print('time: %s'%time.time())


loop = asyncio.get_event_loop()
for i in range(5):
    loop.run_until_complete(func())