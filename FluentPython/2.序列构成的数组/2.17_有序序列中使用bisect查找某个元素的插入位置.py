# python 标准库的bisect 提供了二分算法
# 使用 bisect来进行搜索
# 1. 在有序序列中使用 bisect 查找某个元素的插入位置
import bisect
import sys
Haystack = [1,4,5,6,8,12,15,20,21,23,26,29,30]
Needles = [0,1,2,5,8,10,22,23,29,30,31]
Row_Fmt = '{0:2d} @ {1:2d}  {2}{0:<2d}'
def demo(bisect_fn):
    for needle in reversed(Needles):
        position = bisect_fn(Haystack, needle)   # 在 haystack 中找出 needle 的位置
        offset = position * '   |'
        print(Row_Fmt.format(needle, position, offset))

if __name__=="__main__":
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect.__name__)
    print('haystack—>', '  '.join('%2d'%n for n in Haystack))
    demo(bisect_fn)
