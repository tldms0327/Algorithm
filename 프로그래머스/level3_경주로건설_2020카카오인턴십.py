from collections import deque

inf = int(1e9)


def solution(board):
    size = len(board)
    # to left, up, right, bottom 각각 저장
    dp = [[[inf, inf, inf, inf] for _ in range(size)] for _ in range(size)]
    dp[0][0] = [0, 0, 0, 0]
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # left, up, right, bottom

    queue = deque()
    queue.append([0, 0, -1])  # x, y, direction, preX, preY

    while queue:
        x, y, direction = queue.popleft()
        cost = dp[y][x][direction]
        # i는 방향, d는 방향에 해당하는 좌표
        for i, d in enumerate(directions):
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < size and 0 <= ny < size and board[ny][nx] == 0:
                # 이전과 같은 방향으로 갈 때
                if direction < 0 or direction == i:
                    new_cost = cost + 100  # direction으로 한 칸 나아가 직선도로 건설
                # 다른 방ㅇ향으로 갈 때
                else:
                    new_cost = cost + 600  # direction으로 한 칸 나아가 직선도로 건설

                # new_cost가 더 적을 때만 cost 업데이트, queue에 넣기
                if new_cost < dp[ny][nx][i]:
                    dp[ny][nx][i] = new_cost
                    queue.append([nx, ny, i])

    answer = min(dp[-1][-1])

    return answer


b = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0]]
print(solution(b))
