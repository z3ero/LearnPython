# 分析，既然最终结果要 h1 < h2 < h3 < ...  所有  i-1<=hi<h(i+1) 个方块的
def fun(n, m, hi_list):
    for i in range(n):
        tmp_count=hi_list[i]-i  # 看这个位置还差多少能到达底限值，即需要小易补多少？
        m += tmp_count    # 多了，m增加，少了m较少
        if m<0:
            return 'NO'   # 到了m不够的时候，就说明无法完成
    return 'YES'

T = int(input().strip())
for i in range(T):
    n, m = list(map(int, input().strip().split(' ')))
    hi_list = list(map(int, input().strip().split(' ')))
    print(fun(n,m, hi_list))