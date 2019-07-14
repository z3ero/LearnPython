# 使用 insort在有序序列中，插入元素，保持有序序列的顺序
# insort 原理:
# 1. 先用  bisect 二分找出插入位置
# 2. 在插入元素

import bisect
import random

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->'%new_item, my_list)