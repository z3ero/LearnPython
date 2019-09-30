N, W = list(map(int, input().strip().split()))
w_list = list(map(int, input().strip().split()))
t_list = list(map(int, input().strip().split()))
res_t = 0
cur_w = 0
new_t_list = []
new_w_list = []
i = 0
while i < N:
    while i<N and cur_w + w_list[i] <= W:
        cur_w += w_list[i]
        new_w_list.append(w_list[i])
        new_t_list.append(t_list[i])
        i += 1
    # 装满之后，找出第一批过桥的试试
    min_val = min(new_t_list)
    tmp_len = len(new_t_list)
    tmp_w_list = []
    tmp_t_list = []
    for j in range(tmp_len):
        new_t_list[j] -= min_val
        if new_t_list[j] == 0:
            cur_w -= new_w_list[j]
        else:
            tmp_w_list.append(new_w_list[j])
            tmp_t_list.append(new_t_list[j])
    res_t += min_val
    new_w_list = tmp_w_list
    new_t_list = tmp_t_list
res_t += max(new_t_list)
print(res_t)



