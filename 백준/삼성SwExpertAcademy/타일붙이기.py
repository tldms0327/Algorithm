import sys


def TileSpace(n):
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 3
    dp[3] = 6
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + (dp[i - 2] * 2) + dp[i - 3]

    return dp


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다. 6 3* 2 3*6
cases = []
for test_case in range(1, T + 1):
    cases.append(int(input()))

DP = TileSpace(max(cases))

for idx, c in enumerate(cases):
    print(f"#{idx+1} {DP[c]}")
