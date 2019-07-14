import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    # in 方法
    def __contains__(self, key):
        return str(key) in self.data    # UserDict 内部的data成员变量是 dict 的实例

    def __setitem__(self, key, value):
        self.data[str(key)] = value

# Userdict 继承自 MutableMapping 和 Mappin, 自带 get, update 等方法，不需要重写 get 方法

strkeydict = StrKeyDict()
strkeydict[3] = 300
strkeydict[4] = 400
print(strkeydict)
print(strkeydict.get(4))
print(strkeydict.get(5))