import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
# 表示 5 个 短整数 的10个字节
print(octets)