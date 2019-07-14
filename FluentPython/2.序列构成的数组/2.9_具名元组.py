# 具名元组: 有字段名的元组
# 普通元组是一条没有字段名的记录
# 1. 定义和使用具名元组
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', '1m', (35.689722, 139.87654))
print(tokyo)
print('tokyo 所在国家: %s'%tokyo.country)
print('tokyo 人口: %s'%tokyo.population)
print('tokyo 经纬度: %f, %f\n'%tokyo.coordinates)

# 2. 具名元组的属性和方法
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
beijing_data = ('Beijing', 'CN', '10m', (36.80, 116.79))
Beijing = City._make(beijing_data)
print(Beijing._asdict())
