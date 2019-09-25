n, m=list(map(int,input().strip().split(' ')))
# A最多能拿多少次？
stack = [(1, n, m)]
count = 0.0
while len(stack)>0:
    # A 拿到的概率
    s, n, m = stack.pop()
    if n+m<=0 or m<0:
        continue
    count += s*n/(n+m)
    # A 没有拿到， B和C也没有拿到的概率
    if n+m<=2:
        continue
    new_s = (s*m/(n+m))*((m-1)/(n+m-1))*((m-2)/(n+m-2))
    stack.push((new_s,n,m-3))
    # A 没有拿到， B没拿到，C拿到了的概率
    new_s = (s * m / (n + m)) * ((m - 1) / (n + m - 1)) * (n / (n + m - 2))
    n -= 1
    if n>0:
        stack.append((new_s, n, m-2))
print("%.05f"%count)




