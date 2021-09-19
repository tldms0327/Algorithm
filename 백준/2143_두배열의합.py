from collections import defaultdict

t = int(input())
n = int(input())
A = tuple(map(int, input().split()))
m = int(input())
B = tuple(map(int, input().split()))

arr1 = defaultdict(int)
arr2 = defaultdict(int)
for i in range(n):
    arr1[A[i]] += 1
    summ = A[i]
    for j in range(i + 1, n):
        summ += A[j]
        arr1[summ] += 1

for i in range(m):
    arr2[B[i]] += 1
    summ = B[i]
    for j in range(i + 1, m):
        summ += B[j]
        arr2[summ] += 1
answer = 0
for a in arr1:
    b = t - a
    if arr2[b] > 0:
        answer += arr1[a] * arr2[b]

print(answer)
