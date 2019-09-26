T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    miss_list = list(map(int, input().strip().split(' ')))
    max_value, cur_value = 0, 0
    # 每次把 miss_list[0:k] 分成3段
    lower_dict = {}
    higher_dict = {}
    equal_num = 1
    # 每次看下一个相对于前人的变化
    pre_num = 0
    for k in range(1, n):
        if miss_list[k] == miss_list[k - 1]:
            cur_value += pre_num
            eqaul_num += 1
        elif miss_list[k] > miss_list[k - 1]:
            # 前面有数字比他小
            pre_num += equal_num
            lower_dict[miss_list[k - 1]] = equal_num
            equal_num = 1
            # 只看前面比前任大的数字就可以
            for each in higher_dict:
                if each == miss_list[k]:
                    pre_num += higher_dict[each]
                    equal_num += higher_dict[each]
                    higer_dict.pop(each)
                elif each < miss_list[k]:
                    pre_num += 2 * higer_dict[each]
                    lower_dict[each] = higer_dict[each]
                    higher_dict.pop(each)
        else:
            # 前面的数字比这个大
            pre_num -= equal_num
            higher_dict[miss_list[k - 1]] = equal_num
            equal_num = 1
            # 只看前面比前任小的数字就可以
            for each in lower_dict:
                if each == miss_list[k]:
                    pre_num -= lower_dict[each]
                    equal_num += lower_dict[each]
                    lower_dict.pop(each)
                elif each > miss_list[k]:
                    pre_num -= 2 * lower_dict[each]
                    higher_dict[each] = lower_dict[each]
                    lower_dict.pop(each)

        cur_value += pre_num
        if cur_value > max_value:
            max_value = cur_value

    print(max_value, cur_value)