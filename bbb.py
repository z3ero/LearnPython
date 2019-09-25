import numpy as np

m1=np.matrix([[1, 1, 1, 0, 1],
              [1, 0, 0, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 1, 1]])
#
#m2
# 行平均
tmp1 = m1/m1.sum(axis=1)

# 列平均
m1_t = m1.transpose()
tmp2 = m1_t/m1_t.sum(axis=1)


print(tmp1)
print('---------')
print(tmp2)


ass_m = tmp1.dot(tmp2)
print(ass_m)