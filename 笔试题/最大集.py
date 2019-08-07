import sys
from array import array
n = int(sys.stdin.readline().strip())
points = []
for i in range(n):
    a,b = list(map(int, sys.stdin.readline().strip().split(' ')))
    points.append(array('i', [a,b]))

# 按照 x 进行一次排序
res_ixs = []
max_y = -1
points.sort(key=lambda x: x[0], reverse=True)
for i in range(n):
    if points[i][1] > max_y:
        res_ixs.append(i)
        max_y= points[i][1]
for index in res_ixs[::-1]:
    print("%d %d"%(points[index][0], points[index][1]))