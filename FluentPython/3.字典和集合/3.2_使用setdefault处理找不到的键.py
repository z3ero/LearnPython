index = {'ab':[1,2,3], 'cd':[5,6,7,8]}
ll = [('ab', 8), ('cd', 0), ('ef', 9)]

# 普通的方法将 ll 插入 index
# 需要经过两次 hash 查询
for tp in ll:
    index_l = index.get(tp[0], [])  # 从 index 中找到 tp[0] 对应的映射，没有则返回 []
    index_l.append(tp[1])   # 将新的 tp[0] 映射关系，加入到原先的映射关系
    index[tp[0]] = index_l
print(index)

# 使用setdefault
for tp in ll:
    index.setdefault(tp[0], []).append(tp[1])  # 同上原理，但是会比上面少一次 hash 查询
print(index)


# 使用 collection 中的 defaultdict, 基于dict的__missing__特殊方法，当__getitem__找不到键时，自动调用default_factory
# defaultdict 自动实现了，上述的setdefault方法
