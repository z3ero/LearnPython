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
# 本质上 run_until_complete方法将协程对象包装成一个任务对象，task 对象是Future类的子类，保存了协程运行后的状态，用于未来获取协程的结果
loop.run_until_complete(coroutine)

end = time.time()
print("time is", end-start)