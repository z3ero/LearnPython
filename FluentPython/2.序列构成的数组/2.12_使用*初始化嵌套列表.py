# 错误例子
res = [['_']*3]*3
print(res)
res[0][0]='X'
print(res)    # 内部3个list是同一个引用

# 正确初始化嵌套列表——使用列表推导
res = [['_']*3 for i in range(3)]
print(res)
res[0][0]='Y'
print(res)