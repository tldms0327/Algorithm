from collections import defaultdict
import heapq as hq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    hq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = hq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                hq.heappush(queue, [distance, adjacent])

    return distances


N, M, X = map(int, input().split())

Graph = defaultdict(dict)
for i in range(M):
    a, b, t = map(int, input().split())
    Graph[a][b] = t

distance_from_x = dijkstra(Graph, X)

# 사람별로 X까지 왕복하는 거리 저장하기
answer = [0 for x in range(N + 1)]

for i in range(1, N + 1):
    answer[i] += distance_from_x[i]  # X -> i
    answer[i] += dijkstra(Graph, i)[X]  # i -> X

print(max(answer))
