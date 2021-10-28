import sys

sys.setrecursionlimit(10 ** 6)


def next_spot(x, y, d, grid):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    nx = x + directions[d][0]
    ny = y + directions[d][1]

    if nx >= len(grid):
        nx = 0
    elif nx < 0:
        nx = len(grid) - 1

    if ny >= len(grid[0]):
        ny = 0
    elif ny < 0:
        ny = len(grid[0]) - 1

    return nx, ny


def dfs(state, start, route, grid):
    x = state[0]
    y = state[1]
    d = state[2]
    visited[d][x][y] = 1

    nx, ny = next_spot(x, y, d, grid)
    value = grid[nx][ny]

    if value == 'R':
        d = (d + 5) % 4

    elif value == 'L':
        d = (d + 7) % 4

    if start[0] == nx and start[1] == ny and start[2] == d:
        answer.append(route)
        return

    if not visited[d][nx][ny]:
        dfs([nx, ny, d], start, route + 1, grid)


def solution(grid):
    global answer, visited
    answer = []
    visited = [[[0] * len(grid[0]) for _ in range(len(grid))] for _ in range(4)]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for direction in range(4):
                dfs([x, y, direction], [x, y, direction], 1, grid)

    return sorted(answer)


print(solution(["SL", "LR"]))
