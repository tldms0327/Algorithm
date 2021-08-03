def solution(n, results):
    answer = 0
    graph = {i: [float('inf') if k != i else 0 for k in range(n)] for i in range(n)}
    # 승패 결과 저장
    for r in results:
        a, b = r
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = -1

    distance = floyd_warshall(n, graph)
    for i in range(n):
        if float('inf') not in distance[i]:
            answer += 1

    return answer


def floyd_warshall(n, graph):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if (graph[a][b] == float('inf') or graph[b][a] == float('inf')) and graph[a][c] + graph[b][c] == 0:
                    graph[a][b] = graph[a][c]
                    graph[b][a] = graph[b][c]
    return graph


# n = 5
# lst = [[1, 2], [2, 3]]
# lst = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# print(solution(n, lst))

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]]), 4)
print(solution(6, [[1,2], [2,3], [3,4], [4,5], [5,6]]), 6)
print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
print(solution(3, [[1,2],[1,3]]), 1)
print(solution(6, [[1,6],[2,6],[3,6],[4,6]]), 0)
print(solution(8, [[1,2],[3,4],[5,6],[7,8]]),0)
print(solution(9, [[1,2],[1,3],[1,4],[1,5],[6,1],[7,1],[8,1],[9,1]]), 1)
print(solution(6, [[1,2],[2,3],[3,4],[4,5],[5,6],[2,4],[2,6]]), 6)
print(solution(4, [[4,3],[4,2],[3,2],[3,1],[4,1], [2,1]]), 4)
print(solution(3,[[3,2],[3,1]]), 1)
print(solution(4, [[1,2],[1,3],[3,4]]), 1)
