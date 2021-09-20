import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

n = int(input())
nodes = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [False for _ in range(n + 1)]
visited[1] = True
answer = [0 for _ in range(n + 1)]


def dfs(tree, root):
    children = tree[root]
    for c in children:
        if not visited[c]:
            answer[c] = root
            visited[c] = True
            dfs(tree, c)


dfs(nodes, 1)
for i in range(2, n + 1):
    print(answer[i])
