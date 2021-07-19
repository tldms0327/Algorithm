from collections import defaultdict
import heapq as hq


def solution(N, road, K):
    graph = defaultdict(dict)
    for r in road:
        n1, n2, w = r
        # 두 마을을 연결하는 도로가 여러개 있을 때 최단거리로 저장
        if n1 in graph[n2]:
            graph[n2][n1] = min(graph[n2][n1], w)
            graph[n1][n2] = min(graph[n1][n2], w)
        else:
            graph[n2][n1] = w
            graph[n1][n2] = w

    # 길 찾으면서 최단거리 업데이트 ( 다익스트라! )
    distance = [float('inf')] * (N + 1)  # 1번 마을에서의 거리 저장
    distance[0], distance[1] = 0, 0
    queue = []
    hq.heappush(queue, [distance[1], 1])
    while queue:
        curr_dist, curr_node = hq.heappop(queue)

        if distance[curr_node] < curr_dist:
            continue
        for adj_node, weight in graph[curr_node].items():
            adj_dist = curr_dist + weight
            if adj_dist < distance[adj_node]:
                distance[adj_node] = adj_dist
                hq.heappush(queue, [adj_dist, adj_node])

    return sum([1 for x in distance if x <= K]) - 1  # 0번 마을은 제외


n = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
k = 3
print(solution(n, road, k))
