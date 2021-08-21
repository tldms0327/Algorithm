# gold 4
import sys
from collections import deque

N, M = map(int, input().split())
GRID = []
for _ in range(N):
    GRID.append(list(map(int, sys.stdin.readline().split())))


def check_blank(n, m, grid):
    # 치즈로 둘러싸인 부분 외에 공간은 모두 -1로 표시
    # -1과 맞닿은 부분만 치즈에 영향을 미친다.
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    grid[0][0] = -1
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for spot in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            xx, yy = spot
            if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy] and grid[xx][yy] != 1:
                visited[xx][yy] = True
                grid[xx][yy] = -1
                q.append([xx, yy])
    return grid


def cheese(n, m, grid):
    answer = 0
    done = 0

    grid = check_blank(n, m, grid)
    while True:
        # 시간이 지날 때마다 갱신되는 치즈
        next_grid = list()
        next_grid.append([-1] * m)
        for x in range(1, n - 1):
            next_line = [-1]
            for y in range(1, m - 1):
                # 외부에 노출된 칸이 2개 이상이면 -1로 체크
                if grid[x][y] == -1:
                    done += 1
                    next_line.append(-1)
                elif (grid[x - 1][y], grid[x + 1][y], grid[x][y + 1], grid[x][y - 1]).count(-1) >= 2:
                    next_line.append(-1)
                # 노출이 덜 됐거나, 0인 칸(치즈로 둘러싸인 빈칸)은 패스
                else:
                    next_line.append(grid[x][y])
            next_grid.append(next_line + [-1])
        next_grid.append([-1] * m)
        grid = check_blank(N, M, next_grid)

        if done == (n - 2) * (m - 2):
            break
        else:
            done = 0
        answer += 1
    return answer


print(cheese(N, M, GRID))
