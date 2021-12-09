# 주어진 정수 N과 K에 대하여, N개의 색으로 구성되어 있는 색상환 (N색상환)에서
# 어떤 인접한 두 색도 동시에 선택하지 않으면서 서로 다른 K개의 색을 선택하는 경우의 수를 구하는 프로그램을 작성하시오.

def solution(n, k):
    if k > n // 2 + n % 2:
        return 0
    elif k == 1:
        return n

    # dp[i][j] : i개로 구성된 일직선에서 i번째 j 개의 색을 선택하는 경우의 수
    dp = [[0, i] + [0 for x in range(i // 2)] for i in range(n + 1)]

    for i in range(2, n):
        for j in range(2, len(dp[i])):
            dp[i + 1][j] = dp[i - 1][j - 1] + dp[i][j]

    return dp[n][k]


N = int(input())
K = int(input())
# 첫번째 칸을 선택한 경우 + 선택하지 않은 경우
print((solution(N - 3, K - 1) + solution(N - 1, K)) % 1000000003)
