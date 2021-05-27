import sys

# dp[0] 값을 0으로 초기화하기 위해 앞에 빈칸 추가
s1 = ' ' + input().strip()
s2 = ' ' + input().strip()

dp = [[0 for a in range(len(s1))] for b in range(len(s2))]

for a in range(1, len(s1)):
    for b in range(1, len(s2)):
        # 글자가 같을 땐 이전 lcs +1 로 업데이트
        if s1[a] == s2[b]:
            dp[b][a] = dp[b-1][a-1] + 1
        # 같지 않을 땐 해당 글자와 그 전 글자에서 lcs 찾아서 업데이트
        else:
            dp[b][a] = max(dp[b-1][a], dp[b][a-1])

print(dp[-1][-1])