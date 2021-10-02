def solution(size, street, l):
    answer = True
    history = [1, street[0], False]  # 해당 층의 연속된 개수, 층의 높이, 이 층이 시작됐을 때 왼쪽에 더 높은 층이 있었는지
    for num in street[1:]:
        pre_num = history[1]
        # 같은 놈이면 개수만 더하기
        if num == pre_num:
            history[0] += 1
        # 높이자 2 이상이면 바로 리턴
        elif abs(num - pre_num) > 1:
            return False
        # 한 칸 차이나는 지점에서 경사로 건설 가능성 판단
        else:
            # 현재 칸이 더 높을 때
            if num > pre_num:
                # 높 -> 낮 -> 높 일 땐 '낮'의 길이가 2L 이상이어야 통과 가능
                if history[0] < l or (history[2] and history[0] < 2 * l):
                    return False
                history = [1, num, False]
            # 현재 칸이 더 낮을 때
            else:
                # 높 -> 낮 -> 더낮 일 때 중간 '낮'에 대해서도 판단해야 함
                if history[2] and history[0] < l:
                    return False
                history = [1, num, True]
    if history[2] and history[0] < l:
        answer = False
    return answer


N, L = map(int, input().split())
grid = []
count = 0
for _ in range(N):
    s = list(map(int, input().split()))
    grid.append(s)
    if solution(N, s, L):
        count += 1
for s in zip(*grid):
    if solution(N, s, L):
        count += 1
print(count)
