# 一个简单的二维向量类
# 使用特殊方法实现 向量加法，取模，乘法等操作
from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 字符串表示形式：将一个对象用字符串的形式表示出来，便于辨认
    def __repr__(self):
        return 'Verctor(%r, %r)' % (self.x, self.y)

    # 计算向量的模   hypot 计算直角三角形斜边距离
    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    # 向量的加法
    def __add__(self, other):
        x = self.x + self.x
        y = self.y + self.y
        return Vector(x, y)

    # 向量的乘法
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__=="__main__":
    vec = Vector(3,4)
    print(vec) # 字符串形式打印出来
    print(bool(vec)) # 调用 vec.__bool__ 返回结果
    add_vec = vec + vec
    print(add_vec)
    mul_vec = vec * 3
    print(mul_vec)
