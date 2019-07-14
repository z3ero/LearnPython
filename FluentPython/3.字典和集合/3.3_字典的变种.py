# 特殊的字典，主要包括 collections 中的
from collections import OrderedDict, ChainMap,Counter
# 1. OrderedDict  像栈的字典
# 添加键时保持顺序，popitem() 删除并返回字典最后一个映射，popitem(last)删除并返回第一个映射
order_dict = OrderedDict()
for i in range(10):
    order_dict[i] = str(i*100)
print(order_dict)
print(order_dict.popitem())
print(order_dict.popitem(last=False))
print(order_dict)

# 2. ChainMap 容纳数个映射对象
# 在进行键值查找时，映射对象会被当做一个整体逐个查找，知道键被找到为止
dict_1 = {i: str(i) for i in range(1, 6)}
dict_2 = {i*10: str(i*10) for i in range(1, 6)}
dict_3 = {i*100: str(i*100) for i in range(1, 6)}
chain_map = ChainMap(dict_1, dict_2, dict_3)
print(chain_map)
print(chain_map[500])

# 3. Counter (还可以返回most_common())
ct = Counter("hello world")
print(ct)
print(ct.most_common(2))   # 输出最常见的两个元素



