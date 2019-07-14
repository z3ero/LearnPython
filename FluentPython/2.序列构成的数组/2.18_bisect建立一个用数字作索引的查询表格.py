# 建立一个用数字作索引的查询表格
# 由于使用二分查找，索引查找效率更高
# 需求: 分数 < 60 ---- E
#      60 > 分数 < 70 ---- D
# ...

import bisect
def grade(score, breakpoints=[60,70,80,90], grades='EDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
