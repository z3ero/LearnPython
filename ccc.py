import numpy as np
'''
m = np.array([[0.15, 0.3, 0.2, 0.25, 0.1],
              [0.35, 0.25, 0.15, 0.05, 0.2],
              [0.25, 0.45, 0.05, 0.15, 0.1],
              [0.45, 0.05, 0.25, 0, 0.25],
              [0.05, 0.25, 0.45, 0.2, 0.05],
             ])

print(m)
print(m.sum(axis=1))

res = m
for i in range(20):
    res = res.dot(m)
    print(res)
    print('----------------')
'''
m = np.array([[0.5, 0.5], [0.1, 0.9]])
print(m)
res = m
for i in range(30):
    res = res.dot(m)
    print(res)
    print('----------------')
