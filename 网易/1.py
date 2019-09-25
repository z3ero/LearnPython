n, m = list(map(int, input().strip().split(' ')))
money_dict = {}
money_list = list(map(int, input().strip().split(' ')))
for each in money_list:
    if each in money_dict:
        money_dict[each]+=1
    else:
        money_dict[each]=1
for i in range(m):
    tmp = int(input().strip())
    if tmp in money_dict:
        print(money_dict[tmp])
    else:
        print(0)