n, m = list(map(int, input().strip().split(' ')))
stu_ans_list = []
for i in range(n):
    stu_ans_list.append(list(input().strip()))
score_list = list(map(int, input().strip().split(' ')))
# 思路: 每道题 选择答对最多的人数
from collections import defaultdict

res = 0
for i in range(m):
    tmp_dict = defaultdict(int)
    for j in range(n):
        tmp_dict[stu_ans_list[j][i]] += 1
    max_num = 0
    for key in tmp_dict:
        if tmp_dict[key] > max_num:
            max_num = tmp_dict[key]
    res += max_num * score_list[i]
print(res)