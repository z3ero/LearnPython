# 1. 使用 reduce 和 sum 计算 0~99 之和
from functools import reduce
from operator import add

# reduce: 把某个操作连续应用到序列的元素上，累计之前的结果
print(reduce(add, range(100)))
print(sum(range(100)))

# all 和 any 内置的规约函数
print(all(range(10)))   # 每个元素都是 真值，才返回 True
print(all([]))   # 特例: 空值返回 True

print(any(range(10)))   # 有真值， 就返回 True
print(any([]))   # 特例：空值返回 False

# 使用 reduce 函数和匿名函数 计算阶乘
from functools import reduce
print("10!为%d"%reduce(lambda a,b:a*b, range(1, 10)))

# 使用 reduce 和 operator.mul 函数计算阶乘
from operator import mul
print(reduce(mul, range(1,10)))



