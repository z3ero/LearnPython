k = int(input().strip())
Lib_Str = input().strip()


def fun(Lib_Str, k):
    res = 0
    # 枚举 1 的位置, 开头为 -1， 结尾为 长度
    pos_list = [-1] + [i for i in range(len(Lib_Str)) if Lib_Str[i] == '1'] + [len(Lib_Str)]

    if k == 0:
        # 找1之间的0
        for i in range(len(pos_list) - 1):
            inter = pos_list[i + 1] - pos_list[i] - 1
            res += inter * (inter + 1) / 2
        print(res)
    elif k > len(pos_list) - 2:
        print(0)
    else:
        for i in range(1, len(pos_list) - k):
            j = i + k - 1
            left = pos_list[i] - pos_list[i - 1]
            right = pos_list[j + 1] - pos_list[j]
            res += left * right
        print(res)


fun(Lib_Str, k)

