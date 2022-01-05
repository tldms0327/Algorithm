import sys
from collections import deque as dq

input = sys.stdin.readline


def separated(h, w):
    visited = [row[:] for row in grid]
    queue = dq()
    done = False

    for i in range(h):
        if done:
            break
        for j in range(w):
            if grid[i][j] != 0:
                # 한 덩어리의 시작에서 분기하여 이 덩어리의 visited만 체크r
                done = True
                queue.append((i, j))
                visited[i][j] = 0
                # bfs 시작
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dirr:
                        if 0 <= x + dx < h and 0 <= y + dy < w and visited[x + dx][y + dy] > 0:
                            visited[x + dx][y + dy] = 0
                            queue.append((x + dx, y + dy))
                break

    for row in visited:
        if sum(row) > 0:
            return True

    return False


def yearAfter(h, w):
    global grid
    new_grid = []
    melting = 0
    melted = 0
    for i in range(h):
        new_grid.append([])
        for j in range(w):
            if grid[i][j] == 0:
                new_grid[i].append(0)
            else:
                melting += 1
                count = 0
                for dx, dy in dirr:
                    if 0 <= i + dx < h and 0 <= j + dy < w and grid[i + dx][j + dy] == 0:
                        count += 1
                if grid[i][j] > count:
                    new_grid[i].append(grid[i][j] - count)
                else:
                    new_grid[i].append(0)
                    melted += 1

    grid = new_grid

    return melting == melted


H, W = map(int, input().split())
grid = []

for _ in range(H):
    grid.append(list(map(int, input().split())))

dirr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = 0
all_melted = False
is_separated = separated(H, W)
while not is_separated and not all_melted:
    answer += 1
    all_melted = yearAfter(H, W)
    is_separated = separated(H, W)

if is_separated:
    print(answer)
else:
    print(0)
