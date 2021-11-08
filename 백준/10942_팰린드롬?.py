import sys

read = sys.stdin.readline
n = int(read())
arr = [0] + list(map(int, read().split()))
q = int(read())
dp = [[False for j in range(n + 1)] for _ in range(n + 1)]

# 한자리수는 무조건 팰린드롬
for i in range(1, n + 1):
    dp[i][i] = True
# 두자리수
for i in range(2, n + 1):
    if arr[i - 1] == arr[i]:
        dp[i - 1][i] = True

for s in range(n - 1, 0, -1):
    for e in range(s + 1, n + 1):
        if dp[s + 1][e - 1] and arr[s] == arr[e]:
            dp[s][e] = True

for _ in range(q):
    start, end = map(int, read().split())
    if end < start:
        start, end = end, start
    if dp[start][end]:
        print(1)
    else:
        print(0)
