def factorial(n):
    return 1 if n<2 else n*factorial(n-1)


fact = factorial
print(fact)
fact(5)
print(list(map(fact, range(10))))

# 高阶函数
# 接受函数作为参数，或者 把函数作为结果返回的函数 是 高阶函数
# 如: map, filter, sorted, reduce

