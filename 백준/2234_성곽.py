def solution(grid, m, n):
    room_info = [[-1 for x in range(m)] for y in range(n)]
    room_size = dict()
    room_number = 0
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 남, 동, 북, 서
    for y in range(n):
        for x in range(m):
            # 모든 지점을 돌면서, 아직 방문하지 않은 지점이면 해당 점과 같은 방에 있는 점을 모두 찾고 넘어간다
            if room_info[y][x] < 0:
                room_number += 1
                room_info[y][x] = room_number
                room_size[room_number] = 1

                # 처음 오는 곳이므로 방에 추가하고, 막히지 않은 지점을 bfs로 찾으며
                # 같은 방인 지점 모두 찾고, 방 크기도 동시에 기록하기
                queue = []
                room = grid[y][x]  # 현재 지점
                for i, r in enumerate(room):
                    if r == '0':
                        queue.append([y + directions[i][0], x + directions[i][1]])
                while queue:
                    ny, nx = queue.pop()
                    if room_info[ny][nx] < 0:
                        room = grid[ny][nx]
                        room_info[ny][nx] = room_number
                        room_size[room_number] += 1
                        for i, r in enumerate(room):
                            if r == '0':
                                queue.append([ny + directions[i][0], nx + directions[i][1]])

    # 벽 하나 지웠을 때 생기는 가장 큰 방을 찾기 위해
    # 모든 지점의 옆, 아래 칸을 조사하여 다른 방이면 넓이 비교 범주에 추가한다.
    aj_room = set()  # 인접해 있는 방을 모두 저장
    for y in range(n):
        for x in range(m):
            # 아랫점과 다른 방이면 넓이 비교 set에 넣기
            if y < n - 1 and room_info[y][x] != room_info[y + 1][x]:
                aj_room.add((room_info[y][x], room_info[y + 1][x]))
            # 오른쪽 점
            if x < m - 1 and room_info[y][x] != room_info[y][x + 1]:
                aj_room.add((room_info[y][x], room_info[y][x + 1]))
    # 인접한 방들의 넓이를 합쳐가며 가장 큰 방 크기 찾기
    largest_room = 0
    for room in aj_room:
        if room_size[room[0]] + room_size[room[1]] > largest_room:
            largest_room = room_size[room[0]] + room_size[room[1]]
    return map(str, [len(room_size), max(room_size.values()), largest_room])


M, N = map(int, input().split())
GRID = []
for _ in range(N):
    # 2진수로 바꿔서 넣기
    GRID.append([x[2:].zfill(4) for x in map(lambda x: bin(int(x)), input().split())])
answer = solution(GRID, M, N)
print('\n'.join(answer))
