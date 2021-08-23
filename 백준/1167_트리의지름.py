import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

V = int(input())
TREE = defaultdict(dict)
for _ in range(1, V + 1):
    info = list(map(int, sys.stdin.readline().split()))
    n = info[0]
    for idx, i in enumerate(info[1:-1:2]):
        TREE[n][i] = info[2 * idx + 2]


# 트리에서 임의의 정점에서 루트 노드까지의 거리를 구하는 함수
def longest_node(start, tree, distance):
    now_dist = distance[start]
    for node in tree[start]:
        if distance[node] < 0:
            distance[node] = tree[start][node] + now_dist
            longest_node(node, tree, distance)
    return distance


dist = [-1] * (V + 1)
dist[1] = 0
xy_distance = longest_node(1, TREE, dist)
y = xy_distance.index(max(xy_distance))
dist = [-1] * (V + 1)
dist[y] = 0
yz_distance = longest_node(y, TREE, dist)
print(max(yz_distance))



