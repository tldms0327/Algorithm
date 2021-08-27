import sys
from bisect import bisect_left, bisect_right

N, M, L = map(int, input().split())
H = sorted(list(map(int, input().split())))
A = []
for _ in range(M):
    A.append(map(int, sys.stdin.readline().split()))


def animals(hunters, animal, n, l):
    answer = 0
    for x, y in animal:
        if y > l:
            continue
        else:
            # 이분탐색으로 x와 가장 가까운 사냥꾼 위치 찾기
            idx = bisect_left(hunters, x)
            # 가장 가까운 왼쪽과 오른쪽의 사냥꾼과의 거리가 사정거리 내인지 판단
            if (idx > 0 and x - hunters[idx - 1] <= l - y) or (idx < n and hunters[idx] - x <= l - y):
                answer += 1

    return answer


print(animals(H, A, N, L))
