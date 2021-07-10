import copy
from collections import defaultdict
import heapq as hq


def solution(size, info):
    prev = [[0, size]]
    info = sorted(info, reverse=True)
    answer = 0

    for i, snack in enumerate(info):
        # i 번 스낵의 포함 여부로 다음 단계로 넘어가기
        now = []
        for prev_state in prev:
            # i번 스낵 포함 안함
            now.append(prev_state)
            # i 번 스낵 포함함
            if prev_state[1] >= snack[1]:
                now.append([prev_state[0] + snack[0], prev_state[1] - snack[1]])
            answer = max(answer, prev_state[0], now[-1][0])

        prev = now[:]

    return answer


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    siz, m = map(int, input().split())
    snack_info = []
    for _ in range(m):
        s, p = map(int, input().split())
        snack_info.append([p, s])  # price, size

    price = solution(siz, snack_info)
    print(f"#{test_case} {price}")

