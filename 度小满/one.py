n = int(input().strip())
ai_list = list(map(int, input().strip().split(' ')))
# 思路: 贪心，每次带走尽可能多的血量，所以只在 1~(n-1)/2 范围内出招，(n-1)/2 向上取整
# 从后往前遍历，将每一个都归0
count = 0
for i in range(n, 0, -1):
    if ai_list[i-1] > 0:
        if i % 2 == 1:   # 奇数项，连带前面两项, 注意下标
            count += ai_list[i-1]
            if i-2 >= 0:
                ai_list[i-2] -= ai_list[i-1]
            if i//2-1 >= 0:
                ai_list[i//2-1] -= ai_list[i-1]
            ai_list[i-1] = 0
        else: # 偶数项，连带前面1项
            count += ai_list[i-1]
            if i//2-1 >= 0:
                ai_list[i//2-1] -= ai_list[i-1]
            ai_list[i-1] = 0
print(count)




