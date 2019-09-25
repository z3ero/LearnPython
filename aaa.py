import sys
in_list = list(map(int, sys.stdin.readline().strip().split(' ')))
out_list = list(map(int, sys.stdin.readline().strip().split(' ')))
length = len(in_list)
result_list = [1]*length
for i in range(length-1):
    for j in range(i+1, length):
        if in_list[i] >= in_list[j] and in_list[i]<out_list[j]:
            result_list[i] += 1
            result_list[j] += 1
        if in_list[j] >= in_list[i] and in_list[j]<out_list[i]:
            result_list[i] += 1
            result_list[j] += 1
print(max(result_list))