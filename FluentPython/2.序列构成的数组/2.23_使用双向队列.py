# 双向队列
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print('队列循环右移 3 位:', dq)
dq.rotate(-4)
print('队列循环左移 4 位:', dq)
dq.appendleft(-1)
print('左边入队元素:', dq)
dq.append(899)
print('右边入队元素:', dq)
dq.extendleft([100,200,300])
print('左边批量入队:', dq)
dq.extend([1000,2000,3000])
print('右边批量入队:', dq)

