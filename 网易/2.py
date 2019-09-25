def fun(A, B, p, q):
    # 贪心，每次选择最佳路径， 如果 A+p < B 那么就执行p*q, 否则就执行 A+p
    count = 0
    while A + p < B:
        p *= q
        count += 1
    count += 1
    return count


T = int(input().strip())
for i in range(T):
    A, B, p, q = list(map(int, input().strip().split(' ')))
    print(fun(A, B, p, q))

