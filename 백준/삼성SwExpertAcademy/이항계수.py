def solution(n):
    dp = {0: [1], 1: [1, 1]}
    for i in range(2, n + 1):
        dp[i] = [1 for _ in range(i + 1)]

        for ii in range(1, i):
            dp[i][ii] = dp[i - 1][ii - 1] + dp[i - 1][ii]

    return dp


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
cases = []
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    cases.append([N, A, B])

DP = solution(sorted(cases, reverse=True)[0][0])
for idx, c in enumerate(cases):
    print(f"#{idx + 1} {DP[c[0]][c[1]]}")
