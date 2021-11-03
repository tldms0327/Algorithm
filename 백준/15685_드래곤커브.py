N = int(input())
grid = [[0 for x in range(101)] for y in range(101)]
dirr = [[1, 0], [0, -1], [-1, 0], [0, 1]]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    # gen 0
    grid[y][x] = 1
    nx, ny = dirr[d][0] + x, dirr[d][1] + y
    grid[ny][nx] = 1
    stack = [[nx, ny, d]]
    next_stack = [[nx, ny, d]]
    # gen 1 ~
    for i in range(g):
        while stack:
            x, y, sd = stack.pop()  # 나아갈 방향
            sx, sy, d = next_stack[-1]  # 시작점(바로 전 좌표)
            nd = (sd + 1) % 4
            nx, ny = sx + dirr[nd][0], sy + dirr[nd][1]
            grid[ny][nx] = 1
            next_stack.append([nx, ny, nd])
        stack = next_stack[:]

answer = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] + grid[i + 1][j] + grid[i][j + 1] + grid[i + 1][j + 1] == 4:
            answer += 1
print(answer)
