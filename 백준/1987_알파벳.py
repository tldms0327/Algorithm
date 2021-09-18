import sys


def dfs(grid, x, y, visited, grid_visited):
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    visited[grid[x][y]] = True
    grid_visited[x][y] = True
    global count
    count += 1

    for d in directions:
        nx, ny = d[0] + x, d[1] + y
        if grid[nx][ny] is None or grid_visited[nx][ny]:
            continue
        if not visited[grid[nx][ny]]:
            dfs(grid, nx, ny, visited, grid_visited)
        else:
            global answer
            answer = max(answer, count)

    visited[grid[x][y]] = False
    grid_visited[x][y] = False
    count -= 1


R, C = map(int, input().split())
GRID = [[None for _ in range(C + 2)]]
for _ in range(R):
    GRID.append([None] + list(sys.stdin.readline().strip()) + [None])
GRID.append([None for _ in range(C + 2)])
V = {x: False for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
GV = [[False for y in range(C + 2)] for x in range(R + 2)]
count = 1
answer = 1
dfs(GRID, 1, 1, V, GV)
print(answer - 1)
