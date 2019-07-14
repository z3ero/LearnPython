# 使用列表推导计算笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# 先按颜色排列，再按照尺码排列
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
