n, m = list(map(int, input().strip().split(' ')))
sale_list = list(map(int, input().strip().split(' ')))
for i in range(m):
    sign, w, v = input().strip().split(' ')
    w, v = int(w), int(v)
    if sign == 'Q':
        print(sum(sale_list[w:v])//(v-w+1))
    elif sign == 'U':
        sale_list[w] += v