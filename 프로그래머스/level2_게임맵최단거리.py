def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    nexts = [[0, 0]]
    visited[0][0] = True

    while nexts:
        # heapq로 하려고 했는데 좌표값이 작은게 우선순위가 아니라 fifo가 돼야 함
        # x, y = hq.heappop(nexts)
        # pop(0)해서 효율성 통과 못할줄 알았는데 하네..?
        x, y = nexts.pop(0)
        for d in directions:
            if 0 <= x + d[0] < n and 0 <= y + d[1] < m:
                x1, y1 = x + d[0], y + d[1]
                if not visited[x1][y1] and maps[x1][y1] != 0:
                    visited[x1][y1] = True
                    # maps에 거리 저장
                    maps[x1][y1] += maps[x][y]
                    nexts.append([x1,y1])

    return maps[n - 1][m - 1] if visited[n - 1][m - 1] else -1


