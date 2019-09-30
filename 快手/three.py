n = int(input().strip())
w_list = list(map(int, input().strip().split(' ')))
final_res_w = set()


def fun(arrs):
    L = len(arrs)
    # 任选两块，形成新的 arrs, 进行递归
    for i in range(L - 1):
        for j in range(i + 1, L):
            if arrs[i] < arrs[j]:
                tmp = arrs[j] - arrs[i]
            elif arrs[i] > arrs[j]:
                tmp = arrs[i] - arrs[j]
            else:
                tmp = 0
            new_arrs = []
            if tmp != 0:
                new_arrs.append(tmp)
            for k in range(L):
                if k != i and k != j:
                    new_arrs.append(arrs[k])
            if len(new_arrs) == 0:
                final_res_w.add(0)
            elif len(new_arrs) == 1:
                final_res_w.add(new_arrs[0])
            else:
                fun(new_arrs)


fun(w_list)
print(len(final_res_w))


def fun(arrs):
    L = len(arrs)
    # 任选两块，形成新的 arrs, 进行递归
    for i in range(L - 1):
        for j in range(i + 1, L):
            if arrs[i] < arrs[j]:
                tmp = arrs[j] - arrs[i]
            elif arrs[i] > arrs[j]:
                tmp = arrs[i] - arrs[j]
            else:
                tmp = 0
            new_arrs = []
            if tmp != 0:
                new_arrs.append(tmp)
            for k in range(L):
                if k != i and k != j:
                    new_arrs.append(arrs[k])
            if len(new_arrs) == 0:
                final_res_w.add(0)
            elif len(new_arrs) == 1:
                final_res_w.add(new_arrs[0])
            else:
                fun(new_arrs)


fun(w_list)
print(len(final_res_w))

