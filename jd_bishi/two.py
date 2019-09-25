import sys

n = int(input())
H = list(map(int, sys.stdin.readline().strip().split(' ')))
# 生成元组序列
t_list = []
for i in range(n):
    t_list.append((H[i], i))

# 按值升序排序
val_list = sorted(t_list, key=lambda x: x[0])

# 按下标升序排序
index_list = sorted(t_list, key=lambda x: x[1])

# 找组数
sign_dict = set()  # 表示有没有找过这个数
count = 0
for i in range(0, n-1):
    if val_list[i] in sign_dict:
        continue
    sign_dict.add(val_list[i])
    count += 1
    # 从下标数组中找
    for j in range(val_list[i][1]+1,n):
        if index_list[j][0] <= val_list[i+1][0]:
            sign_dict.add(index_list[j])

if val_list[-1] not in sign_dict:
    count += 1
print(count)