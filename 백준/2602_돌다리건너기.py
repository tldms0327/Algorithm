# dp[천사, 악마][다리index][두루마리에 적힌 문자열 index]
# 소형기관차였나 그거랑 거의 똑같은 문제

target = input().strip()
angel = input().strip()
devil = input().strip()
bridge_size, target_size = len(angel), len(target)
# 다리의 첫 칸의 왼쪽에 0을 하나 넣어서(bridge_size + 1) indexError 방지
dp = [[[0 for a in range(len(target))] for b in range(bridge_size + 1)] for c in range(2)]

# dp[x][i][0] 초기화
for i in range(1, bridge_size + 1):
    dp[0][i][0] = dp[0][i - 1][0] + 1 if angel[i - 1] == target[0] else dp[0][i - 1][0]
    dp[1][i][0] = dp[1][i - 1][0] + 1 if devil[i - 1] == target[0] else dp[1][i - 1][0]

for j in range(1, target_size):
    for i in range(1, bridge_size + 1):
        # if devil[i-1] == target[j]:
        #     dp[1][i][j] = dp
        dp[0][i][j] = dp[1][i - 1][j - 1] + dp[0][i - 1][j] if angel[i - 1] == target[j] else dp[0][i - 1][j]
        dp[1][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j] if devil[i - 1] == target[j] else dp[1][i - 1][j]

print(dp[0][-1][-1] + dp[1][-1][-1])
