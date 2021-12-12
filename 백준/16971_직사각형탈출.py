from collections import deque as dq


def isMovePossible(grid, sr, sc, n, m, h, w):
    for r in range(sr - 1, sr + h):
        for c in range(sc - 1, sc + w):
            if not (0 <= r < n and 0 <= c < m) or grid[r][c] == 1:
                print(r, c)
                return False
    return True


N, M = map(int, input().split())
Grid = [list(map(int, input().split())) for _ in range(N)]
# 직사각형의 크기 H, W, 시작 좌표 Sr, Sc, 도착 좌표 Fr, Fc
# 1 ≤ r ≤ N, 1 ≤ c ≤ M
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[0 for i in range(M)] for j in range(N)]
visited[Sr - 1][Sc - 1] = 0
queue = dq()
queue.append([Sr, Sc, 0])

while queue:
    sr, sc, count = queue.pop()
    for d in directions:
        nr, nc = sr + d[0], sc + d[1]
        if visited[nr - 1][nc - 1] == 0:
            visited[nr - 1][nc - 1] = count + 1
            if isMovePossible(Grid, nr, nc, N, M, H, W):
                queue.append([nr, nc, count + 1])
print(visited)
print(visited[Fr - 1][Fc - 1])
