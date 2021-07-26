import heapq
from math import ceil


def solution(n, m, l, d):
    d.sort()
    dist = [d[0], l - d[-1]]
    for i in range(len(d) - 1):
        dist.append(d[i + 1] - d[i])

    hq = [[-1 * i, -1 * i, 1] for i in dist]
    heapq.heapify(hq)

    while m > 0:
        # dist_value는 현재 휴개소가 없는 가장 긴 거리,
        # origin_dist는 휴게소를 새로 짓기 전의 거리,
        # divider는 원래 거리에서 몇 번 나뉘었는지 저장
        dist_value, origin_dist, divider = heapq.heappop(hq)
        # 휴게소는 정수에만 세울 수 있으므로 ceil
        divider += 1
        new_dist_value = ceil(-1 * origin_dist / divider)
        heapq.heappush(hq, [-1 * new_dist_value, origin_dist, divider])

        m -= 1

    return -1 * heapq.heappop(hq)[0]


N, M, L = map(int, input().split())
D = list(map(int, input().split()))
print(solution(N, M, L, D))
