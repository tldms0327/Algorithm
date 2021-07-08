def solution(n, grid):
    size = 2
    answer = 0
    moving = True
    moving_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # find first position of the fish
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 9:
                x, y = i, j
                grid[i][j] = 0
                break
    eat_count = 0
    visiting = set()
    for dir in moving_direction:
        if 0 <= x + dir[0] < n and 0 <= y + dir[1] < n:
            visiting.add((x + dir[0], y + dir[1], 1))
    eatable_fish = []

    while moving:
        visit_done = set()
        visit_done.add((x, y))
        while visiting:
            x1, y1, dist = visiting.pop()
            if grid[x1][y1] <= size:
                for dir in moving_direction:
                    x2 = x1 + dir[0]
                    y2 = y1 + dir[1]
                    if 0 <= x2 < n and 0 <= y2 < n and (x2, y2) not in visit_done:
                        visiting.add((x2, y2, dist + 1))
            if 0 < grid[x1][y1] < size:
                eatable_fish.append([x1, y1, dist])

            visit_done.add((x1, y1))

        if not eatable_fish:
            moving = False
        else:
            eat = sorted(eatable_fish, key=lambda k: (k[2], k[0], k[1]))[0]
            answer += eat[2]
            x, y = eat[0], eat[1]
            grid[x][y] = 0
            visiting.clear()
            for dir in moving_direction:
                if 0 <= x + dir[0] < n and 0 <= y + dir[1] < n:
                    visiting.add((x + dir[0], y + dir[1], 1))

            eatable_fish = []
            eat_count += 1

            if eat_count == size:
                size += 1
                eat_count = 0

    return answer


N = int(input())
GRID = []
for _ in range(N):
    GRID.append(list(map(int, input().split())))

print(solution(N, GRID))
