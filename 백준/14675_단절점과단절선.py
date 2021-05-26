# 단절점과 단절선
import sys
from collections import defaultdict

graph = defaultdict(int)
answer = []

# 한 노드에 연결된 노드가 몇개인지 확인하기
n = int(input())
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a] += 1
    graph[b] += 1

# 트리구조이므로 모든 엣지가 단절선
# 노드에 연결된 노드가 2개 이상이면 무조건 단절점
m = int(input())
for i in range(m):
    t, k = map(int, input().split())
    if t == 2:
        answer.append("yes")
    elif t == 1:
        if (graph[k]) >= 2:
            answer.append("yes")
        else:
            answer.append("no")

for a in answer:
    print(a)
