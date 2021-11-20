def dfs(x, y, depth, path):
    if depth == N:
        # 확률계산
        global answer
        path_prob = 1
        for p in path:
            path_prob *= probs[p] / 100
        answer += path_prob
        return

    for idx, d in enumerate(directions):
        nx, ny = x + d[0], y + d[1]
        if not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx, ny, depth + 1, path + [idx])
            visited[ny][nx] = False
        else:
            continue
    return


inputs = list(map(int, input().split()))
N, PROBS = inputs[0], inputs[1:]
directions = []
probs = []
for i, prob in enumerate(PROBS):
    if prob != 0:
        directions.append([[1, 0], [-1, 0], [0, 1], [0, -1]][i])
        probs.append(prob)

visited = [[False for _ in range(30)] for _ in range(30)]
visited[14][14] = True
answer = 0
dfs(14, 14, 0, [])
print(answer)
