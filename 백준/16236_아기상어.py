from collections import deque
import heapq as hq


def solution(n, grid):
    size = 2
    answer = 0
    moving = True
    # find first position of the fish
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 9:
                x, y = i, j
                grid[i][j] = 0
                break

    q = deque()
    q.append((x, y, 0))
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    min_dist = []  # (dist, x,y) 형태로 저장
    visited = set()
    fish_count = 0

    while moving:
        while q:
            x, y, dist = q.popleft()
            visited.add((x, y))
            for dx, dy in dirs:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < n and 0 <= y1 < n and (x1, y1) not in visited:
                    visited.add((x1, y1))

                    # 다음 칸으로 이동 가능
                    if grid[x1][y1] in [0, size]:
                        q.append((x1, y1, dist + 1))
                        continue
                    # 이동할 수 없는 경우
                    elif grid[x1][y1] > size:
                        continue
                    else:
                        # min_dist.append((dist+1, x1, y1))
                        hq.heappush(min_dist, (dist + 1, x1, y1))  # 힙큐가 쪼오끔 더 빠름
        if min_dist:
            dist, x, y = min_dist[0]
            # dist, x, y = sorted(min_dist, key=lambda k: (k[0], k[1], k[2]))[0]
            answer += dist
            fish_count += 1
            grid[x][y] = 0

            if fish_count == size:
                size += 1
                fish_count = 0
            q.clear()
            q.append((x, y, 0))
            min_dist = []  # (dist, x,y) 형태로 저장
            visited = set()
        else:
            moving = False

    return answer


N = int(input())
GRID = []
for _ in range(N):
    GRID.append(list(map(int, input().split())))

print(solution(N, GRID))
