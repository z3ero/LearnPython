import sys

n = int(input())
s = sys.stdin.readline().strip()
mode = True   # 小写模式
times = 0
for i in range(0, n-1):
    tmp = (s[i] >= 'a')
    if tmp == mode: # 模式匹配
        times += 1
    else:   # 模式不匹配
        tmp_1 = (s[i+1] >= 'a')
        if tmp_1 == tmp:    # 后一个与前一个都是大（小）写， 长期改
            times += 2
            mode = not mode
        else:   # 不相同，短期改
            times += 2

# 到了最后一个
if (s[-1]>='a')^mode:
    times += 2
else:
    times += 1







# 遍历找出 大写 和 小写 字母的长度分别为多少
big_num = 0
small_num = 0
for c in s:
    if c < 'a':
        big_num += 1
    else:
        small_num += 1
# 一个比较优的方案，临时上制
if big_num > small_num:
    min_times = 1 + big_num + 2 * small_num  # 开始就切大写
else:
    min_times = small_num + 2 * big_num  # 开始不切换

start_mode = True  # 表示小写模式
times = 0


def digui(s, start_mode, times):
    if len(s) == 1:
        if s[0] >= 'a' == start_mode:  # 当前字符和当前模式匹配
            times += 1
        else:
            times += 2  # 不匹配
    else:  #
        if s[0] >= 'a' == start_mode:  # 模式匹配







