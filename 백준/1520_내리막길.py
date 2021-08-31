# 골드5, dfs + dp 문제
import sys

sys.setrecursionlimit(10 ** 6)


def dfs(sx, sy, grid, dp):
    if dp[sx][sy] != -1:
        return dp[sx][sy]

    temp = 0
    for nx, ny in [[sx - 1, sy], [sx + 1, sy], [sx, sy - 1], [sx, sy + 1]]:
        if grid[nx][ny] < grid[sx][sy]:
            temp += dfs(nx, ny, grid, dp)
    dp[sx][sy] = temp
    return dp[sx][sy]


N, M = map(int, input().split())
GRID = [[10000] * (M + 2)]
for _ in range(N):
    GRID.append([10000] + list(map(int, input().split())) + [10000])
GRID.append([10000] * (M + 2))
dp = [[-1] * (M + 2) for _ in range(N + 2)]
dp[N][M] = 1

print(dfs(1, 1, GRID, dp))
