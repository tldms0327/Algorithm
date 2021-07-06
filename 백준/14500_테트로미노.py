def solution(grid, n, m):
    answer = 0
    # I
    for i in range(n):
        for j in range(m):
            if i < n - 3:
                answer = max(answer, grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j])
            if j < m - 3:
                answer = max(answer, sum(grid[i][j:j + 4]))
    # ㅁ
    for i in range(n - 1):
        for j in range(m - 1):
            answer = max(answer, grid[i][j] + grid[i + 1][j] + grid[i][j + 1] + grid[i + 1][j + 1])

    # L, ㅏ (가운데 3칸 주변 6칸을 보고 가장 큰 것 찾기)
    for i in range(n):
        for j in range(m):
            k, t = 0, 0

            # I + 튀어나온 부분
            if i < n - 2:
                k = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
                if j == 0:
                    t = max(grid[i][j + 1], grid[i + 1][j + 1], grid[i + 2][j + 1])
                elif j == m - 1:
                    t = max(grid[i][j - 1], grid[i + 1][j - 1], grid[i + 2][j - 1])
                else:
                    t = max(grid[i][j + 1], grid[i + 1][j + 1], grid[i + 2][j + 1], grid[i][j - 1], grid[i + 1][j - 1],
                            grid[i + 2][j - 1])
            answer = max(answer, k + t)

            if j < m - 2:
                k = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                if i == 0:
                    t = max(grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2])
                elif i == n - 1:
                    t = max(grid[i - 1][j], grid[i - 1][j + 1], grid[i - 1][j + 2])
                else:
                    t = max(grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2], grid[i - 1][j], grid[i - 1][j + 1],
                            grid[i - 1][j + 2])
            answer = max(answer, k + t)

    # ㄹ
    for i in range(n - 2):
        for j in range(m - 1):
            k = sum(grid[i][j:j + 2]) + sum(grid[i + 1][j:j + 2]) + sum(grid[i + 2][j:j + 2])
            answer = max(answer, k - grid[i][j] - grid[i + 2][j + 1], k - grid[i][j + 1] - grid[i + 2][j])
    for i in range(n - 1):
        for j in range(m - 2):
            k = sum(grid[i][j:j + 3] + grid[i + 1][j:j + 3])
            answer = max(answer, k - grid[i][j] - grid[i + 1][j + 2], k - grid[i][j + 2] - grid[i + 1][j])

    return answer


N, M = map(int, input().split())
GRID = []
for _ in range(N):
    GRID.append(list(map(int, input().split())))

print(solution(GRID, N, M))
