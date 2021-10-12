n = int(input())
spots = []
sum1, sum2 = 0, 0
first = list(map(int, input().split()))
x1, y1 = first
for i in range(n - 1):
    x2, y2 = map(int, input().split())
    sum1 += y2 * x1
    sum2 += x2 * y1
    x1, y1 = x2, y2
x2, y2 = first
sum1 += y2 * x1
sum2 += x2 * y1

print(round(abs(sum1 - sum2) / 2, 1))
