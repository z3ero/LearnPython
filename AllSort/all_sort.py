# 尽量在源数据上操作，不使用辅助空间
# 1.冒泡排序
def bubble_sort(arrs):
    length = len(arrs)
    for i in range(length):
        sign = True
        for j in range(0, length-1-i):
            if arrs[j] > arrs[j+1]:
                arrs[j], arrs[j+1] = arrs[j+1], arrs[j]
                sign = False
        if sign is True:
            break
    return arrs

# 2. 插入排序
def insert_sort(arrs):
    length = len(arrs)
    for index in range(0, length-1):
        cur_data = arrs[index+1]
        pre_index = index
        while pre_index >=0 and cur_data < arrs[pre_index]:
            arrs[pre_index+1] = arrs[pre_index]
            pre_index -= 1
        arrs[pre_index+1] = cur_data
    return arrs

# 快速排序
def partition(arrs, start, end):
    key = arrs[start]
    while start < end:
        while start < end and key <= arrs[end]:
            end -= 1
        arrs[start] = arrs[end]
        while start < end and key >= arrs[start]:
            start += 1
        arrs[end] = arrs[start]
    arrs[start] = key
    return start

def quick_sort(arrs, start, end):
    if start < end:
        pos = partition(arrs, start, end)
        quick_sort(arrs, start, pos-1)
        quick_sort(arrs, pos+1, end)
    return arrs

if __name__=="__main__":
    arrs = [69, 76, 43, 52, 36, 78, 23, 12]
    print(bubble_sort(arrs.copy()))
    print(insert_sort(arrs.copy()))
    print(quick_sort(arrs.copy(), 0, len(arrs)-1))
