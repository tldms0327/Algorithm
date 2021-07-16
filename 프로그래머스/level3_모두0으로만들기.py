from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)


def dfs(tree, a, node, visited):
    global answer
    visited[node] = True
    for child in tree[node]:
        if not visited[child]:
            leaf_weight = dfs(tree, a, child, visited)
            a[node] += leaf_weight
            answer += abs(leaf_weight)

    return a[node]


def solution(a, edges):
    global answer
    answer = 0
    if sum(a) != 0:
        return -1

    tree = defaultdict(list)
    for e in edges:
        tree[e[0]].append(e[1])
        tree[e[1]].append(e[0])

    visited = [False] * len(a)
    dfs(tree, a, 2, visited)
    return answer

    # while a.count(0) != len(a):
    #     visited_tree = defaultdict(set)
    #     for t in tree:
    #         nodes = tree[t]
    #         if len(nodes) == i:  # 자식이 없는 노드
    #             while nodes:
    #                 connected = nodes.pop()
    #                 a[connected] += a[t]
    #                 answer += abs(a[t])
    #                 a[t] = 0
    #                 print(a, tree)
    #                 visited_tree[connected].add(t)
    #                 # tree[parent].remove(t)
    #     for t in tree:
    #         tree[t] = tree[t] - visited_tree[t]
    #     # i += 1
    #     print(i, a, tree, answer)

    # return answer


a = [-5, 0, 2, 1, 2, 0]
e = [[0, 1], [3, 4], [2, 3], [0, 3], [0, 5]]
print(solution(a, e))
