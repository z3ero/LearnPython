import inspect
'''
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
print(inspect.getmro(D))
'''

class D(object):
    pass
class E(object):
    pass
class F(object):
    pass
class C(D, F):
    pass
class B(E, D):
    pass
class A(B, C):
    pass
print(A.mro())