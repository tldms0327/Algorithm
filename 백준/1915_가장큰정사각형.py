n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, list(input()))))

# 맨 왼쪽, 위쪽은 grid와 같이 초기화
dp = [grid[0]] + [[0 if x != 0 else grid[y][0] for x in range(m)] for y in range(1, n)]
for y in range(1, n):
    for x in range(1, m):
        if grid[y][x] == 0:
            continue
        else:
            # 주변이 0이 아니면 해당 칸이 추가되면서 생기는 가장 큰 사각형 크기로 업데이트
            if dp[y - 1][x] > 0 and grid[y - 1][x - 1] > 0 and grid[y][x - 1] > 0:
                dp[y][x] = min(dp[y][x - 1], dp[y - 1][x], dp[y - 1][x - 1]) + 1
            # 주변에 0이 있으면 1(나 자식)로 업데이트
            else:
                dp[y][x] = 1
# 가장 큰 정사각형의 한 변의 크기 찾기
answer = max([max(line) for line in dp])
print(answer ** 2)
