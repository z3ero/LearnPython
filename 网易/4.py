T = int(input().strip())
for i in range(T):
    n, k = list(map(int, input().strip().split(' ')))
    hi_list = list(map(int, input().strip().split(' ')))
    # start_index = 0
    # print(fun(start_index, n, k, hi_list))
    dp_list = [[False] * 2 for i in range(n)]  # n 行 2列的矩阵，列0表示没有超能力，列1表示有超能力
    # 从 n开始往前演
    dp_list[n - 1][0] = True
    dp_list[n - 1][1] = True
    for w in range(n - 2, -1, -1):
        end = min(n, w+k+1)
        for v in range(w + 1, end):  # 能跳到的范围
            if hi_list[v] <= hi_list[w]:  # 不用超能力
                dp_list[w][0] = dp_list[w][0] or dp_list[v][0]
                dp_list[w][1] = dp_list[w][1] or dp_list[v][1]
            else:
                dp_list[w][1] = dp_list[w][1] or dp_list[v][0]  # 使用超能力
    if dp_list[0][1]:
        print('YES')
    else:
        print('NO')