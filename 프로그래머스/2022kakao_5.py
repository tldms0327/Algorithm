from collections import deque, defaultdict
import heapq


def solution(info, edges):
    answer = 0
    visited = [False for _ in range(len(info))]
    visited[0] = True
    tree = defaultdict(list)
    for e in edges:
        tree[e[0]].append(e[1])
    sheep, wolf = 0, 0
    if I[0] == 1:
        sheep += 1
    else:
        wolf += 1


    return answer


I = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
E = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
print(solution(I, E))
