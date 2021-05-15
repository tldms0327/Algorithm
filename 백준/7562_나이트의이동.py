import sys


def solution(N, start, end):
    if start == end:
        return 0

    answer = 0
    grid = [[0 for x in range(N)] for y in range(N)]
    visited = set()
    visited.add(start)

    move_scope = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    while grid[end[0]][end[1]] == 0:
        next_visited = set()
        for v in visited:
            for move in move_scope:
                x, y = v[0] + move[0], v[1] + move[1]
                if 0 <= x < N and 0 <= y < N and grid[x][y] == 0:
                    grid[x][y] = 1
                    next_visited.add((x, y))
        visited = next_visited
        answer += 1
    return answer


# N = 100
# start = (1,1)
# end = (1,1)
answers = []
n = int(sys.stdin.readline())
for _ in range(n):
    size = int(sys.stdin.readline())
    s = tuple(map(int, sys.stdin.readline().split()))
    e = tuple(map(int, sys.stdin.readline().split()))

    answers.append(solution(size, s, e))

for a in answers:
    print(a)
