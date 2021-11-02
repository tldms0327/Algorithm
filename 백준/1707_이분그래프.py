from collections import defaultdict


def bipartite(graph, v, e):
    # v: 정점개수, e: 간선개수
    if e == 0:
        return 'YES'
    visited = [0 for _ in range(v + 1)]
    now_nodes = {1}
    next_nodes = set()
    status = 1

    while True:
        while now_nodes:
            now = now_nodes.pop()
            visited[now] = status
            for node in graph[now]:
                if visited[node] == status:
                    return 'NO'
                elif visited[node] == 0:
                    next_nodes.add(node)
                else:
                    continue
        if not next_nodes:
            for i, n in enumerate(visited):
                if n == 0:
                    now_nodes = {i}
                    status = -status
                    next_nodes = set()
                    break
            if not now_nodes:
                break
        else:
            status = -status
            now_nodes = next_nodes
            next_nodes = set()

    return 'YES'


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    G = defaultdict(list)
    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    print(bipartite(G, V, E))
