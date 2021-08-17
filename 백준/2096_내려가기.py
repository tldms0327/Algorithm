import sys

N = int(input())

# 현재 층에서의 점수들
dp_now = []
for _ in range(N):
    if not dp_now:
        # dp_now 초기화(맨 첫칸)
        input_row = map(int, sys.stdin.readline().split())
        dp_now = [[x, x] for x in input_row]
    else:
        next_row = map(int, sys.stdin.readline().split())
        a, b, c = next_row
        dp_next = [0, 0, 0]
        # 접근할 수 있는 윗칸을 보고 min, max 값 계산하여 저장
        dp_next[0] = [a + min(dp_now[0][0], dp_now[1][0]), a + max(dp_now[0][1], dp_now[1][1])]
        dp_next[1] = [b + min(dp_now[0][0], dp_now[1][0], dp_now[2][0]),
                      b + max(dp_now[0][1], dp_now[1][1], dp_now[2][1])]
        dp_next[2] = [c + min(dp_now[1][0], dp_now[2][0]), c + max(dp_now[1][1], dp_now[2][1])]

        dp_now = dp_next[:]
        dp_next = [0, 0, 0]

print(max([dp_now[i][1] for i in range(3)]), min([dp_now[i][0] for i in range(3)]))
