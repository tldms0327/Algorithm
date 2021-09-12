from collections import deque as dq
from bisect import bisect_left


# 최장 증가 부분 수열 (LIS) 알고리즘

# # 일단 bfs로는 메모리 초과 난다.
# def solution(lst):
#     queue = dq()
#     queue.append([1, lst[0]])
#     queue.append([0, 0])
#     for x in lst[1:]:
#         next_queue = dq()
#         while queue:
#             now = queue.popleft()
#             next_queue.append(now)
#             if now[1] <= x:
#                 next_queue.append([now[0] + 1, x])
#
#         queue = next_queue
#     return sorted(queue, reverse=True)[0][0]

def solution(lst):
    # 이분탐색을 이용해 LIS 를 구해주는 함수
    dp = [lst[0]]
    i = 0
    for x in lst[1:]:
        if dp[i] < x:
            dp.append(x)
            i += 1
        else:
            idx = bisect_left(dp, x)
            dp[idx] = x

    return dp


N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))
lis = solution(numbers)  # 오른차순으로 정렬된 가장 긴 배열 찾기
print(N - len(lis))
