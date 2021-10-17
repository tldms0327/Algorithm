from collections import defaultdict

n = int(input())
num = list(map(int, input().split()))

sums = defaultdict(int)
for i in range(n - 1):
    for j in range(i + 1, n):
        sums[num[i] + num[j]] += 1

answer = 0
zeros = num.count(0)
for x in num:
    if x != 0 and sums[x] > zeros:
        answer += 1

# 0이 하나일 땐 sums[0]가 1 이상이면, 두개일 땐 2 이상이면, 세개 이상일 땐 무조건 가능
if zeros <= 2 and sums[0] >= zeros:
    answer += zeros
elif zeros >= 3:
    answer += zeros

print(answer)
