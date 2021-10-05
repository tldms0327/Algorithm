def solution(rows, columns, queries):
    answer = []
    grid = [[y + x * columns for y in range(1, columns + 1)] for x in range(0, rows)]
    for query in queries:
        answer.append(rotate(grid, query))
        print(grid)

    return answer


def rotate(grid, query):
    x1, y1, x2, y2 = [i - 1 for i in query]
    corners = [grid[x1][y1], grid[x1][y2], grid[x2][y2], grid[x2][y1]]  # 왼쪽 위부터 시계 방향의 꼭지점
    moved_values = corners[:] + grid[x1][y1 + 1:y2] + grid[x2][y1 + 1:y2] + [grid[x - 1][y2] for x in
                                                                             range(x2 + 1, x1 + 1, -1)] + [
                       grid[x + 1][y1] for x in range(x1, x2 - 1)]
    # 윗줄 옮기기
    grid[x1][y1 + 1:y2 + 1] = [corners[0]] + grid[x1][y1 + 1:y2]
    # 아랫줄
    grid[x2][y1:y2] = grid[x2][y1 + 1:y2] + [corners[2]]
    # 오른쪽
    for x in range(x2, x1 + 1, -1):
        grid[x][y2] = grid[x - 1][y2]
    # 왼쪽
    for x in range(x1, x2 - 1):
        grid[x][y1] = grid[x + 1][y1]
    # 코너 채우기
    grid[x1 + 1][y2] = corners[1]
    grid[x2 - 1][y1] = corners[3]

    return min(moved_values)



