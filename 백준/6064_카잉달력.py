from math import gcd
import sys


def lcm(a, b):
    return int(a * b / gcd(a, b))


# 나누기로 접근
def solution(a, b, X, Y):
    lc = lcm(a, b)
    for i in range(int(lc / a) + 1):
        if ((a * i) - Y + X) % b == 0:
            return a * i + X
    return -1


# 단순접근(당연히 시간초과 ㅎㅎ)
# def solution(a, b, X, Y):
#     x, y = 0, 0
#     for i in range(lcm(a, b)):
#         if x < a:
#             x += 1
#         else:
#             x = 1
#         if y < b:
#             y += 1
#         else:
#             y = 1
#         if x == X and y == Y:
#             return i + 1
#     return -1


n = int(input())
answer = []
for _ in range(n):
    a, b, x, y = list(map(int, sys.stdin.readline().split()))
    answer.append(str(solution(a, b, x, y)))

print('\n'.join(answer))
