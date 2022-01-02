# 어차피 홀수는 칸이 안 맞아 불가능
# 2는 3가지로 채울 수 있음
# 4는 2로 쪼개지지 않는 방법으로 채우는 경우만 생각하기 -> 2가지뿐
# 6은 4 + 2(3가지), 2 + 4(2가지), 0 + 6(2가지)
# ... dp[n] = dp[n-2] * dp[2] + ( 1+ dp[2] + dp[4] + ... + dp[n-4]) * 2
n = int(input())

if n % 2 != 0:
    print(0)
else:
    dp = [0 for _ in range(31)]
    dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2
    print(dp[n])
