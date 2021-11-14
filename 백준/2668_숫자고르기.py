n = int(input())
visited = [False for _ in range(n)]
connected = []
answer = []
for i in range(n):
    k = int(input()) - 1
    connected.append(k)
    if i == k:
        visited[i] = True
        answer.append(i)


def cycle(nodes, now, target):
    visited[now] = True
    # 사이클 확인
    if nodes[now] == target:
        return True
    if not visited[nodes[now]]:
        visited[nodes[now]] = True
        is_cycle = cycle(nodes, nodes[now], target)
        if not is_cycle:
            visited[nodes[now]] = False
            visited[now] = False
            return False
        else:
            return True
    else:
        visited[now] = False
        return False


for i in range(n):
    if not visited[i]:
        cycle(connected, i, i)
    else:
        continue

print(visited.count(True))
for i in range(n):
    if visited[i]:
        print(i + 1)
