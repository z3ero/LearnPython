import sys


# 像是大数问题
# 使用相减法: 规则 a-b=0, 则 a = b = 最大公约数
# 判断两个数哪个大
def compare(a, b):
    if len(a) > len(b):
        return True
    elif len(a) == len(b):
        for ai, bi in zip(a, b):
            if ai > bi:
                return True
            elif ai < bi:
                return False
        return False
    else:
        return False

# 对两个大数进行减法，
def sub(a, b):
    carry = 0
    for i in range(1, len(b)+1):
        if a[-i] >= b[-i] + carry:
            a[-i] -= (b[-i] + carry)
            carry = 0
        else:
            a[-i] = a[-i] + 10 - (b[-i] + carry)
            carry = 1
    if carry == 1:
        a[-len(b)-1] -= 1

    tmp_b = b
    b = []
    for index in range(len(a)):
        if a[index] > 0:
            b = a[index: len(a)]
            break
    a = tmp_b
    # 始终保持 a > b
    if not compare(a, b):
        a, b = b, a
    return a,b

if __name__ == "__main__":
    # 读取两个数
    a = list(map(int, list(sys.stdin.readline().strip())))
    b = list(map(int, list(sys.stdin.readline().strip())))
    # 始终保证 a > b
    if not compare(a, b):
        a, b = b, a
    while len(b) > 0:  # b 等于0，跳出循环，a 为最大公约数
        a, b = sub(a, b)
    print(''.join(list(map(str, a))))


