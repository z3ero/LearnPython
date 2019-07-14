# 1. 原字典的改变通过MappingProxyType可以看到
# 2. 无法通过MappingProxyType修改原字典
from types import MappingProxyType
d = {i:str(i*10) for i in range(1,10)}
map_proxy = MappingProxyType(d)
print(map_proxy)
d[4] = '499'
print(map_proxy)
map_proxy[5] = '599'