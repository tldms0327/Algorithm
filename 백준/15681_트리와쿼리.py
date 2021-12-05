import sys
from collections import defaultdict

sys.setrecursionlimit(10000000)


def makeTree(currentNode, parent):
    for child in connect[currentNode]:
        if child != parent:
            tree[currentNode].append(child)
            makeTree(child, currentNode)


def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for child in tree[currentNode]:
        countSubtreeNodes(child)
        size[currentNode] += size[child]


input = sys.stdin.readline
N, R, Q = map(int, input().split())
connect = defaultdict(list)
Queries = []
for _ in range(N - 1):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)
tree = {i: [] for i in range(1, N + 1)}

size = [0 for _ in range(N + 1)]

for _ in range(Q):
    Queries.append(int(input()))

makeTree(R, -1)
countSubtreeNodes(R)

print('\n'.join([str(size[q]) for q in Queries]))
