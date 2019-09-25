# 输入
T = int(input().strip())
for i in range(T):
    n, m = list(map(int, input().strip().split(' ')))
    ai_list = list(map(int, input().strip().split(' ')))

    res_list = [0]*n
    for i in range(1, n):
        sum_count = sum(ai_list[0:i+1])
        j = 0   # 从最大的数开始删除
        while sum_count > m:
            sum_count -= ai_list[j]
            j += 1
        res_list[i] = j    # 第i道题放弃了 j 道
        # 插入排序: 将 第 i 道 插入，保证ai_list[0:i] 严格降序
        # 用堆排序应该更好，一时写不出
        val = ai_list[i]
        insert_index = i-1
        while insert_index >= 0 and ai_list[insert_index] < val:
            ai_list[insert_index+1] = ai_list[insert_index]
            insert_index -= 1
        ai_list[insert_index+1] = val
print(res_list)

# 最后要输出文字  改 print(res_list)
print(' '.join(map(str, res_list)))

