import sys
import operator
from functools import reduce


def nCr(n, r):
    if n < r:
        return 0
    if n - r < r:
        r = n - r
    return reduce(operator.mul, range(n, n - r, -1), 1) // reduce(operator.mul, range(1, r + 1), 1)


# def solution(n):
#     # 점화식: dp[n+1] = dp[n] + (2n-2Cn - 2n-3Cn) = dp[n]
#     dp = [0 for _ in range(n + 1)]
#     dp[1] = 1
#     for i in range(1, n):
#         w, h = i + 1, 0
#         count = 0
#         queue = [[w - 1, 1]]
#         while queue:
#             w, h = queue.pop()
#             if h == 0:
#                 count += dp[w]
#             elif w == 0:
#                 count += 1
#             else:
#                 queue += [[w, h - 1], [w - 1, h + 1]]
#         dp[i + 1] = count
#
#     #     dp[i + 1] = dp[i] + nCr(2 * i - 2, i) - nCr(2 * i - 3, i)
#
#     return dp
def solution(n):
    dp = [dict() for _ in range(2 * n + 1)]
    dp[1] = {1: 1}
    dp[2] = {1: 1, 2: 1}
    if n <= 1:
        return dp
    for i in range(1, n):
        n1, n2 = 2 * i + 1, 2 * i + 2
        # 홀수일 때 먼저 처리
        for k in range(n1 // 2 + 1, n1):
            dp[n1][k] = dp[n1 - 1][k - 1] + dp[n1 - 1][k]
        dp[n1][n1] = 1
        dp[n2][n2] = 1
        dp[n2][n2 // 2] = dp[n1][n2 // 2]
        for k in range(n2 // 2 + 1, n2):
            dp[n2][k] = dp[n1][k - 1] + dp[n1][k]
    return dp


input = sys.stdin.readline
query = []
while True:
    x = int(input())
    if x != 0:
        query.append(x)
    else:
        break

answer = solution(max(query))
for q in query:
    print(answer[2 * q][q])
