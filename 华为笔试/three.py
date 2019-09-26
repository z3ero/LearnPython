T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    miss_list = list(map(int, input().strip().split(' ')))
    max_value, cur_value = 0, 0
    # 思路：每次向后移动一天，对前面的数字排序, 找出前面的数，有多少比当前小，多少比当前大
    for k in range(1, n):
        # 对 第 k 个元素 进行插入排序，找到插入位置
        tmp_val = miss_list[k]
        insert_index = k - 1
        while insert_index >= 0 and miss_list[insert_index] > tmp_val:
            miss_list[insert_index + 1] = miss_list[insert_index]
            insert_index -= 1
        miss_list[insert_index + 1] = tmp_val
        # 再向前看，有多少和它相等的
        equal_num = 0
        for v in range(insert_index, -1, -1):
            if miss_list[v] == tmp_val:
                equal_num += 1
            else:
                break
        # 统计 cur_value 的变化
        cur_value += insert_index + 1 - equal_num  # 加了多少
        cur_value -= k - insert_index - 1  # 减了多少
        if cur_value > max_value:
            max_value = cur_value

    print(max_value, cur_value)