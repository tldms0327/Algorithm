import sys
import heapq as hq
from collections import defaultdict

n = int(input())

heap = []
history = defaultdict(int)
for _ in range(n):
    i = int(sys.stdin.readline())
    # 0이 아닐때
    if not i:
        if not heap:
            print(0)
        else:
            # 절댓값이 제일 작은 수 pop
            k = hq.heappop(heap)
            # 이 음수가 힙에 존재하면 음수로 출력
            if history[abs(k) * -1] > 0:
                print(abs(k) * -1)
                history[abs(k) * -1] -= 1
            # 양수일 땐 그냥 출력
            else:
                print(k)
                history[k] -= 1
    else:
        # heap에 넣을때는 절댓값으로 넣고, 양/음은 따로 기록
        hq.heappush(heap, abs(i))
        history[i] += 1
