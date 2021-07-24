from collections import defaultdict
from collections import deque as dq

N = int(input())
node_info = list(map(int, input().split()))
target = int(input())


def tree_leaf(n, info, t: int):
    answer = 0
    graph = dict()
    root = info.index(-1)
    # 루트를 삭제하면 리프는 없다
    if t == root:
        return 0

    # 그래프 만들기 키: 노드번호, 값: children 노드 리스트
    for i, parent in enumerate(info):
        if parent == -1:
            continue
        else:
            if parent in graph:
                graph[parent].append(i)
            else:
                graph[parent] = [i]
            if i not in graph:
                graph[i] = []

    # bfs로 타겟 노드 밑의 노드를 모두 지워주기
    queue = dq()
    queue.append(target)
    # 타겟의 부모노드에서 타겟 제거
    graph[info[target]].remove(target)

    while queue:
        i = queue.popleft()
        i_children = graph[i]
        for ch in i_children:
            queue += graph[ch]
            del graph[ch]
        del graph[i]

    # 리프 노드 세기
    for node in graph:
        if len(graph[node]) == 0:
            answer += 1

    return answer


print(tree_leaf(N, node_info, target))
