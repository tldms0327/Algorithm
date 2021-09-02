N, K = map(int, input().split())


def solution(n, k):
    # dp[i] : n을 i개로 쪼개는 경우의 수
    dp = [{i: 0 for i in range(1, n + 1)}, {i: 1 for i in range(1, n + 1)}, {i: i + 1 for i in range(1, n + 1)}]
    now_k = 2
    while now_k < k:
        temp = dict()
        temp[1] = now_k + 1
        for i in range(2, n + 1):
            # dp[i][n] = 1+ dp[i-1][1] + dp[i-1][2] ... + dp[i-1][n]
            temp[i] = sum([dp[now_k][x] for x in range(1, i + 1)]) + 1
        dp.append(temp)
        now_k += 1

    return dp[k][n] % 1000000000


print(solution(N, K))
