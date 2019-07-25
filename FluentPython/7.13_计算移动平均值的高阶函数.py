# 计算移动平均值——不保存所有的历史值, 只保存 总数 和 个数
# 错误例：count+=1; total+=new_value 让count, total 变成局部变量
'''
def make_average():
    count = 0
    total = 0

    def averager(new_value):
        count+=1
        total+=new_value
        return total/count

    return averager
'''
# 正确例:
# 使用 nolocal 将变量标记为自由变量，即使在函数中为变量赋新值, 也会变成自由变量
def make_average():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count
    return averager

avg = make_average()
for i in range(10):
    print(avg(i))

