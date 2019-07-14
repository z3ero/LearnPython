# 使用有名字的切片
ori_str = 'abcdefg1234567'
alphas = slice(0, 7)
digits = slice(7, 14)
print(ori_str[alphas], ori_str[digits])

# 多维切片 和 省略
# python 内置的序列类型都是一维的，只支持单一的索引，成对的索引没有用的
# 多维切片一般用于 numpy 这样的外部拓展
import numpy as np
array = np.array([[1,2,3,4,5,6],[10,20,30,40,50,60],[100,200,300,400,500,600]])
print(array[2, 2])
print(array[2,...])
