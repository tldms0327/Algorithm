from collections import deque


def solution(n, info):
    answer = []
    apeach = {i: 0 for i in range(11)}
    apeach_score = 0
    for i, count in enumerate(info):
        apeach[10 - i] = count
        if count > 0:
            apeach_score += 10 - i
    queue = deque()
    # 다음에 알아볼 숫자, 현재 숫자를 쐇는지 여부, 남은 화살, 현재 점수
    queue.append([9, False, n, 0, apeach_score])
    if n > apeach[10] > 0:
        queue.append([9, True, n - apeach[10] - 1, 10, apeach_score - 10])
    elif apeach[10] == 0:
        queue.append([9, True, n - apeach[10] - 1, 10, apeach_score])
    else:
        queue.append([9, True, 0, 0, apeach_score])

    last_status = []
    while queue:
        now_i, status, left_n, score, now_apeach = queue.popleft()
        if now_i == 0:
            last_status.append(score - now_apeach)
            continue
        queue.append([now_i - 1, False, left_n, score, now_apeach])
        if left_n == 0:
            queue.append([now_i - 1, True, 0, score, now_apeach])
        elif left_n > apeach[now_i] > 0:
            queue.append([now_i - 1, True, left_n - apeach[now_i] - 1, score + now_i, now_apeach - now_i])
        elif apeach[now_i] == 0:
            queue.append([now_i - 1, True, left_n - 1, score + now_i, now_apeach])
        else:
            queue.append([now_i - 1, True, 0, 0, now_apeach])
    max_score = converter(last_status.index(max(last_status)))

    if max(last_status) <= 0:
        return [-1]
    for i, x in enumerate(max_score[:-1]):
        if x == '1':
            answer.append(apeach[10 - i] + 1)
            n -= apeach[10 - i] + 1
        else:
            answer.append(0)
    answer.append(n)

    return answer


def converter(x):
    answer = ''
    while x > 0:
        answer += str(x % 2)
        x //= 2
    return answer[::-1].zfill(10) + '0'


N = 9
I = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
# [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]
print(solution(N, I))
