import heapq
from collections import defaultdict


def find(x, parent):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    if x == y:
        return
    else:
        parent[y] = x
    return


while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    edges = []
    parent = [i for i in range(M + 2)]
    total_cost = 0

    for _ in range(N):
        a, b, w = map(int, input().split())
        total_cost += w
        heapq.heappush(edges, (w, a, b))

    answer = 0
    cnt = 0
    while cnt < M - 1:
        w, s, e = heapq.heappop(edges)
        if find(s, parent) != find(e, parent):
            union(s, e, parent)
            answer += w
            cnt += 1

    print(total_cost - answer)
