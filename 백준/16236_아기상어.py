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

    eat_count = 0  # size일 때 먹은 물고기 수 기록
    visiting = set()  # 앞으로 방문해봐야 하는 좌표를 거리와 함께 기록
    visiting.update([(x - 1, y, 1), (x, y - 1, 1), (x, y + 1, 1), (x + 1, y, 1)])  # 사방 한칸씩 이동
    possible_fish = []  # 현 위치에서 먹을 수 있는 물고기 기록

    while moving:
        # 이미 방문한 좌표
        visit_done = set()
        visit_done.add((x, y))

        while visiting:
            x1, y1, dist = visiting.pop()
            if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n:
                continue
            else:
                visit_done.add((x1, y1))
                # 옆이 0이거나 같아서 나아갈 수 있을 때
                if grid[x1][y1] <= size:
                    # 사방 4곳 중 안 가본 곳만 추가
                    for spot in [(x1 - 1, y1), (x1, y1 - 1), (x1, y1 + 1), (x1 + 1, y1)]:
                        if spot not in visit_done:
                            visiting.add(spot + (dist + 1,))
                # 이 물고기를 먹을 수 있으면 주변은 더 탐색 안함
                if 0 < grid[x1][y1] < size:
                    possible_fish.append([x1, y1, dist])

        if not possible_fish:
            moving = False
        else:
            # 거리, 위, 왼쪽으로 정렬
            now = sorted(possible_fish, key=lambda l: (l[2], l[0], l[1]))[0]
            answer += now[2]

            x, y = now[0], now[1]
            grid[x][y] = 0
            visiting.clear()
            visiting.update([(x - 1, y, 1), (x, y - 1, 1), (x, y + 1, 1), (x + 1, y, 1)])
            possible_fish = []
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
