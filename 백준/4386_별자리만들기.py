import math


def get_parent(i):
    if cycle_info[i] != i:
        cycle_info[i] = get_parent(cycle_info[i])
    return cycle_info[i]


def union(a, b):
    a = get_parent(a)
    b = get_parent(b)
    cycle_info[a], cycle_info[b] = min(a, b), min(a, b)


N = int(input())
nodes = []
for _ in range(N):
    nodes.append(tuple(map(float, input().split())))

distance_info = []
cycle_info = [i for i in range(N)]
answer = 0
for a in range(N - 1):
    for b in range(a + 1, N):
        x1, y1 = nodes[a]
        x2, y2 = nodes[b]
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        distance_info.append([dist, a, b])
distance_info.sort()

for node in distance_info:
    # union-find를 이용한 크루스칼 알고리즘
    min_dist, x, y = node
    # find
    x_parent = get_parent(x)
    y_parent = get_parent(y)
    if x_parent != y_parent:
        answer += min_dist
        # union
        union(x, y)


print(round(answer, 2))

