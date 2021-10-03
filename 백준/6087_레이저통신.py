from collections import deque

inf = int(1e9)
W, H = map(int, input().split())
C = []
grid = []
for h in range(H):
    line = list(input())
    temp = []
    for w, x in enumerate(line):
        if x == '.':
            temp.append(0)
        elif x == '*':
            temp.append(1)
        else:
            temp.append(0)
            C += [h, w]
    grid.append(temp)


start_x, start_y, end_x, end_y = C
dp = [[[inf, inf, inf, inf] for _ in range(W)] for _ in range(H)]
dp[start_x][start_y] = [0, 0, 0, 0]
# up, left, bottom, right
directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
queue = deque()
queue.append([start_x, start_y, -1])  # x, y, direction

while queue:
    x, y, direction = queue.popleft()
    cost = dp[x][y][direction]
    # i는 방향, d는 방향에 해당하는 좌표
    for i, d in enumerate(directions):
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == 0:
            if direction < 0 or direction == i:
                new_cost = cost
            else:
                new_cost = cost + 1  # 거울 설치
            # new_cost가 더 적을 때만 cost 업데이트, queue에 넣기
            if new_cost < dp[nx][ny][i]:
                dp[nx][ny][i] = new_cost
                queue.append([nx, ny, i])

answer = min(dp[end_x][end_y])
print(answer)
