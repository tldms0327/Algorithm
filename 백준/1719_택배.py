from collections import defaultdict
import heapq as hq


def first_next_node(graph, start):
    # 다익스트라 알고리즘을 이용하여 start에서 각 노드로 가는 최단거리 경로를 찾기

    # start에서 각 지점까지의 최단거리 저장
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # 도착지 노드로 가는 최단경로 중 도착지 노드 바로 전 노드를 저장해두기
    end_path = {i: i for i in graph}
    queue = []
    hq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = hq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance  # 거리 업데이트
                end_path[adjacent] = current_node  # end의 바로 전 노드 업데이트
                hq.heappush(queue, [distance, adjacent])

    next_node_info = dict()
    for i in graph:
        # start는 '-'
        if i == start:
            next_node_info[i] = '-'
        # 도착지로 가기 전 노드가 start면 start와 인접한 가까운 노드이므로 자기 자신으로 기록
        elif end_path[i] == start:
            next_node_info[i] = i
        else:
            # 바로 전 노드부터 타고 올라 가면서 start - end 경로 중 첫번째 노드 찾기
            x = i
            while end_path[x] != start:
                x = end_path[x]
            next_node_info[i] = x

    return next_node_info


n, m = map(int, input().split())
graph = defaultdict(dict)
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w

for k in range(1, n + 1):
    answer = first_next_node(graph, k)
    print(' '.join(map(str, [answer[i] for i in range(1, n + 1)])))
