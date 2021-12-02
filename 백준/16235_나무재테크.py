import sys
from collections import deque

input = sys.stdin.readline


def year_later(trees, foods, size):
    adjacents = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    next_trees = [[deque() for _ in range(size)] for _ in range(size)]
    next_foods = [[0 for i in range(size)] for j in range(size)]
    count_tree = 0

    # 봄, 여름, 가을, 겨울 한번에 처리하기
    for y in range(size):
        for x in range(size):
            died = 0
            if trees[y][x]:
                tree = trees[y][x]
                while tree:
                    age = tree.popleft()
                    # 나무가 봄에 죽지 않고 가을까지 번식할 수 있을 때
                    if foods[y][x] >= age:
                        foods[y][x] -= age
                        next_trees[y][x].append(age + 1)
                        count_tree += 1
                        if (age + 1) % 5 == 0:
                            for adj in adjacents:
                                ny, nx = y + adj[0], x + adj[1]
                                if 0 <= ny < size and 0 <= nx < size:
                                    next_trees[ny][nx].appendleft(1)
                                    count_tree += 1
                    else:
                        died += age // 2
            # 여름에 죽은 나무의 양분, 겨울이 지나고 추가될 양분
            next_foods[y][x] = died + foods[y][x] + A[y][x]

    return next_trees, next_foods, count_tree


N, M, K = map(int, input().split())
A = []
TREES = [[deque() for _ in range(N)] for _ in range(N)]
FOODS = [[5 for i in range(N)] for j in range(N)]
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    r, c, age = map(int, input().split())
    TREES[r - 1][c - 1].append(age)
for _ in range(K):
    TREES, FOODS, answer = year_later(TREES, FOODS, N)

# print(TREES)
# print(FOODS)
print(answer)
