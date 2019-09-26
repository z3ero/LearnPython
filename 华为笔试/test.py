T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    miss_list = list(map(int, input().strip().split(' ')))
    max_value, cur_value = 0, 0
    # 对miss_list 按照 value 排序依次
    tmp_dict = {i: miss_list[i] for i in range(n)}
    index_value = sorted(tmp_dict.items(), key=lambda x:x[1])
    for k in range(1, n):
        count_1 = 0
        count_2 = 0
        for v in range(k):
            if index_value[v][0] < index_value[k][0]:
                if index_value[v][1] == index_value[k][1]:
                    count_1 += 1
                else:
                    count_2 += 1
        cur_value += count_2 - (k-count_2 - count_1)
        if cur_value > max_value:
            max_value = cur_value
    print(max_value, cur_value)