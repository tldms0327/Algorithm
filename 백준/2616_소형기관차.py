n = int(input())
arr = list(map(int, input().split()))
k = int(input())

k_sums = [sum(arr[i:i + k]) for i in range(n - k + 1)]
# print(k_sums)  # len k_sums: n - k + 1
# 객차가 0, 1, 2 개일때 운반할 수 있는 사람 수
dp = [[0, 0, 0] for i in range(n - k + 1)]

# 소형 기관차 1대일 때의 dp
dp[0][0] = k_sums[0]
for i in range(n - k):
    dp[i + 1][0] = max(k_sums[i + 1], dp[i][0])

# 소형 기관차 2대일 때의 dp
# 초기화
for i in range(k):
    dp[i][1] = dp[i][0]
# dp
for i in range(k - 1, n - k):
    dp[i + 1][1] = max(dp[i - k + 1][0] + k_sums[i + 1], dp[i][1])

# 소형 기관차 3대일 때의 dp
for i in range(2 * k):
    dp[i][2] = dp[i][1]
for i in range(2 * k - 1, n - k):
    dp[i + 1][2] = max(dp[i - k + 1][1] + k_sums[i + 1], dp[i][2])

print(dp[-1][2])
