import sys


def DSLR(s, flag=None):
    result = dict()
    num = int(s)
    # D
    if num * 2 >= 10000:
        result['D'] = num * 2 % 10000
    else:
        result['D'] = num * 2
    # S
    if num == 0:
        result['S'] = 9999
    else:
        result['S'] = num - 1
    # L, R
    x1 = num // 1000  # 1000 자리
    x2 = (num % 1000) // 100  # 100 자리
    x3 = (num % 100) // 10  # 10 자리
    x4 = num % 10
    # 오른쪽-왼쪽 왔다갔다 하지 않게 flag 이용
    if flag != 'L':
        result['R'] = x4 * 1000 + x1 * 100 + x2 * 10 + x3
    if flag != 'R':
        result['L'] = x2 * 1000 + x3 * 100 + x4 * 10 + x1
    return result


def solution(before, after): # DFS
    after = int(after)
    if before == after:
        return ''

    now = DSLR(before)
    inspected = set()  # visited
    for k in now:
        if now[k] == after:
            return k
        inspected.add(now[k])
    while True:
        nextlevel = dict()
        for k in now:
            temp = DSLR(now[k], flag=k[-1])
            for t in temp:
                val = temp[t]
                if val == after:
                    return k + t
                elif val not in inspected:
                    nextlevel[k + t] = val
                    inspected.add(val)
        now = nextlevel


# string으로 접근하면 시간초과ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
# def DSLR(s, flag=None):
#     result = dict()
#     num = int(s)
#     # D
#     if num * 2 >= 10000:
#         result['D'] = str(num * 2 % 10000).zfill(4)
#     else:
#         result['D'] = str(num * 2).zfill(4)
#     # S
#     if num == 0:
#         result['S'] = '9999'
#     else:
#         result['S'] = str(num - 1).zfill(4)
#     # L, R
#     if flag != 'L':
#         result['R'] = s[-1] + s[:-1]
#     if flag != 'R':
#         result['L'] = s[1:] + s[0]
#     return result
#
#
# def solution(before, after):
#     after = after.zfill(4)
#     before = before.zfill(4)
#
#     if before == after:
#         return ''
#
#     now = DSLR(before)
#     inspected = set()
#     for k in now:
#         if now[k] == after:
#             return k
#         inspected.add(now[k])
#
#     while True:
#         nextlevel = dict()
#         for k in now:
#             temp = DSLR(now[k], flag=k[-1])
#             # print(k, temp)
#             for t in temp:
#                 val = temp[t]
#                 if val == after:
#                     return k + t
#                 elif val not in inspected:
#                     nextlevel[k + t] = val
#                     inspected.add(val)
#         now = nextlevel


i = int(input())
answer = []
for _ in range(i):
    a, b = sys.stdin.readline().split()
    answer.append(solution(a, b))

print('\n'.join(answer))
