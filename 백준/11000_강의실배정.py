import sys
import heapq as hq

input = sys.stdin.readline
n = int(input())
inputs = []

for _ in range(n):
    inputs.append(tuple(map(int, input().split())))
inputs.sort()

end_times = []
rooms = 0
answer = 0
for row in inputs:
    s, e = row

    while end_times and s >= end_times[0]:
        hq.heappop(end_times)
        rooms -= 1

    rooms += 1
    hq.heappush(end_times, e)
    if answer < rooms:
        answer = rooms
print(answer)

# for _ in range(n):
#     s, e = map(int, input().split())
#     timeline[s] += 1
#     timeline[e] -= 1
#     if e > max_time:
#         max_time = e
#
# answer = 0
# temp = timeline[0]
# for i in range(1, max_time):
#     temp += timeline[i]
#     if temp > answer:
#         answer = temp
#
# print(answer)
