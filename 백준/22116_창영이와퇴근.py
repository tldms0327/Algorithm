import sys
from collections import deque


def target_possible(target):
    visited = [[False for i in range(size)] for j in range(size)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < size and 0 <= ny < size and not visited[ny][nx] and abs(grid[ny][nx] - grid[y][x]) <= target:
                if nx == size - 1 and ny == size - 1:
                    return True
                else:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

    return False


size = int(input())
grid = []
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for _ in range(size):
    grid.append(list(map(int, sys.stdin.readline().split())))

if size == 1:
    print(0)
else:
    left, right = 0, 1000000000
    while left <= right:
        mid = (left + right) // 2
        if target_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)
