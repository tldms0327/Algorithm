import time

n = int(input())
start = time.time()
dp = [[0, 0] for i in range(n + 1)]
visited = [True, True] + [False for i in range(n - 1)]
dp[1] = [1, 1]
step = 1
next_num = {(1, 2), (1, 3)}
while not visited[n]:
    temp = []
    for (prev, nex) in next_num:
        if nex <= n and not visited[nex]:
            visited[nex] = True
            dp[nex] = [prev, nex]
            temp += [(nex, nex + 1), (nex, nex * 2), (nex, nex * 3)]
    next_num = set(temp)

cnt = 0
answer = str(n)
i = n
while i != 1:
    cnt += 1
    answer += ' ' + str(dp[i][0])
    i = dp[i][0]
end = time.time()
print(cnt, answer.strip(), sep='\n')
print(end - start)
