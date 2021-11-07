# 프로그래머스 level3 순위랑 유사한 문제
import sys
from collections import defaultdict


def floyd_warshall(n, graph):
    for a in range(n):
        for b in range(n):
            for c in list(graph[a]):
                if c in graph[b]:
                    if graph[a][c] + graph[b][c] == 0 and (
                            b not in graph[a] or a not in graph[b]):
                        graph[a][b] = graph[a][c]
                        graph[b][a] = graph[b][c]
            # for c in range(n):
            #     if (c in graph[a] and c in graph[b]) > 0 and graph[a][c] + graph[b][c] == 0 and (
            #             b not in graph[a] or a not in graph[b]):
            #         graph[a][b] = graph[a][c]
            #         graph[b][a] = graph[b][c]
    return graph


N, M = map(int, input().split())
# GRAPH = {i: [2000 if i != j else 0 for j in range(N)] for i in range(N)}
GRAPH = defaultdict(dict)
for _ in range(M):
    small, big = map(int, sys.stdin.readline().split())
    GRAPH[small - 1][big - 1] = -1
    GRAPH[big - 1][small - 1] = 1

floyd_warshall(N, GRAPH)
answer = 0
for i in range(N):
    if len(GRAPH[i]) == N - 1:
        answer += 1

print(answer)
