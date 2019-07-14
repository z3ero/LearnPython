# 数组: 一个浮点数组的创建, 存入文件和从文件读取的过程
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

# 浮点数组写入文件
fp = open('./data/floats.bin', 'wb')
floats.tofile(fp)
fp.close()

# 从文件中读取浮点数组
floats2 = array('d')
fp = open('./data/floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()

print(floats2[-1])
print(floats==floats2)
