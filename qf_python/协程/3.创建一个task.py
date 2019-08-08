import time
import asyncio

# 定义了一个协程
async def run(x):
    print("waiting: %d"%x)

start = time.time()
# 得到一个协程对象，这个时候run函数不执行
coroutine = run(2)
print(coroutine)

# 创建一个事件循环（从asyncio模块中获取了一个引用）
loop = asyncio.get_event_loop()
# 将协程对象加入到事件循环中
# loop.run_until_complete(coroutine)

# 创建任务 两种方式
task = asyncio.ensure_future(coroutine)
# task = loop.create_task(coroutine)
print(task)
# 将任务加入到事件循环中
loop.run_until_complete(task)

end = time.time()
print("time is", end-start)