import sys


def sol(m, n, h, box):
    # m:가로, n: 세로, h: 높이, grid[h][]
    visited = set()
    day = 0
    count = 0
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if box[z][y][x] == 1:
                    visited.add((z, y, x))
                    count += 1

                elif box[z][y][x] == -1:
                    count += 1

    if len(visited) == 0:
        return -1

    while count < m * n * h:
        visited_add = set()
        for v in visited:
            z, y, x = v[0], v[1], v[2]
            if x >= 1 and box[z][y][x - 1] == 0:
                box[z][y][x - 1] = 1
                visited_add.add((z, y, x - 1))
            if x < m - 1 and box[z][y][x + 1] == 0:
                box[z][y][x + 1] = 1
                visited_add.add((z, y, x + 1))
            if y >= 1 and box[z][y - 1][x] == 0:
                box[z][y - 1][x] = 1
                visited_add.add((z, y - 1, x))
            if y < n - 1 and box[z][y + 1][x] == 0:
                box[z][y + 1][x] = 1
                visited_add.add((z, y + 1, x))
            if z >= 1 and box[z - 1][y][x] == 0:
                box[z - 1][y][x] = 1
                visited_add.add((z - 1, y, x))
            if z < h - 1 and box[z + 1][y][x] == 0:
                box[z + 1][y][x] = 1
                visited_add.add((z + 1, y, x))

        if len(visited_add) == 0:
            day = -1
            break
        count += len(visited_add)
        visited = visited_add
        day += 1
        print(visited)

    return day


m, n, h = list(map(int, sys.stdin.readline().split()))
box = []
grid = []
for i in range(h):
    for k in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        grid.append(temp)
    box.append(grid)
    grid = []

print(sol(m, n, h, box))