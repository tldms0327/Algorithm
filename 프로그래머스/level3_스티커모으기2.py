def solution(sticker):
    n = len(sticker)
    if n <= 3:
        return max(sticker)

    # 그리디 알고리즘으로 풀어보자
    # 1.
    # 첫 번째 칸을 선택한 경우, 맨 마지막 칸은 선택할 수 없으므로 마지막에서 두 번째 칸까지만 탐색
    summ = [0] * n
    summ[0] = sticker[0]
    for i in range(2, n - 1):
        summ[i] = max(summ[i - 2], summ[i - 3]) + sticker[i]
    answer = max(summ)

    # 2.
    # 첫 번째 칸을 선택하지 않았을 때
    summ = [0] * n
    summ[1] = sticker[1]
    for i in range(2, n):
        summ[i] = max(summ[i - 2], summ[i - 3]) + sticker[i]
    answer = max(answer, max(summ))

    return answer


print(solution([1, 3, 2, 5]))
