from collections import defaultdict
import sys


# Floyd - Warshall Algorithm
def min_dist(graph, size):
    for pass_node in range(size):
        for start in range(size - 1):
            for end in range(start + 1, size):
                pass_distance = graph[start][pass_node] + graph[end][pass_node]
                if graph[start][end] > pass_distance:
                    graph[start][end] = pass_distance
                    graph[end][start] = pass_distance

    return graph


s, q = map(int, input().split())
g = dict()
for n in range(s):
    g[n] = [float('inf') if i != n else 0 for i in range(s)]

for _ in range(q):
    a, b = map(int, sys.stdin.readline().split())
    g[a - 1][b - 1] = 1
    g[b - 1][a - 1] = 1

min_dist(g, s)
print(g)
kevin = sorted(g.items(), key=lambda x: sum(x[1]))[0][0]

print(kevin + 1)

