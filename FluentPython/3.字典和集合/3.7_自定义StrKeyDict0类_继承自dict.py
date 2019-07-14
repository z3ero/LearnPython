# 实现 StrKeyDict0 类，给定 key 查询时，（key为数字时）按照字符串来查询
# 这里自定义该类——继承自dict
class StrKeyDict0(dict):
    # __missing__ 特殊方法, 只有在调用 __getitem__ 即 [key] 时，key 不存在时，才触发
    def __missing__(self, key):
        if isinstance(key, str):   # 若 key 是字符串，key 仍不存在，则抛异常
            raise KeyError
        return self[str(key)]   # key 不为字符串，转为字符串查询

    # get 方法委托 给 dict的__getitem__方法，以便触发 __missing__ 方法，若有异常，则返回默认值None
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):   # 注意： self.keys() 在python2 中返回是 list, python3 返回是set
        return key in self.keys() or str(key) in self.keys()

if __name__=="__main__":
    str_key_dict0 = StrKeyDict0()
    str_key_dict0['3'] = 300
    str_key_dict0['8'] = 800
    print('3 is str_key_dict0:', 3 in str_key_dict0)
    print(str_key_dict0.get(8))
    print(str_key_dict0.get(9))
