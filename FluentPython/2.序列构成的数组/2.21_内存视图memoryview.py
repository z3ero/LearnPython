from array import array
# 'h' 两个字节的有符号数   第一个字节是低位，第二个字节是高位
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print("数组长度为: %d"%len(memv))
print(memv[0])
# 将内存视图的内容转化为 'B' 类型，一个字节的无符号数
memv_oct = memv.cast('B')
print(memv_oct.tolist())   # 这一个 list的长度是 原先数组长度 的 2倍
# 将 第 3 个数字的高位 赋值 4， 则第三个数字变为 1024 = 2**(2+8)
memv_oct[5] = 4
print(numbers)

