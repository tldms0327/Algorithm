N = int(input())
# i 번째 행의 몇 번째 열에 퀸이 있는지 기록 / n-queen 문제에서 모든 행에 퀸이 하나씩 존재하니까!
QUEENS = [0 for _ in range(N)]
answer = 0


# recursionlimimt을 함부로 걸지 말자! 메모리를 미리 할당해두기 때문에 메모리 초과가 날 수 있다.
# 내가 한 건 글로벌 변수를 줄이기 위해서인데, 그냥 글로벌로 선언해 두는게 속도 면에서는 더 낫다.


def N_Queen(queens, n, count):
    global answer
    # n개의 퀸을 다 배치했으면 정답 +1
    if count == n:
        answer += 1
        return answer

    for i in range(n):
        # 퀸이 새로 배치될 수 있는가?
        queen_capable = True
        for j in range(count):
            # 현재 count개의 퀸이 배치된 상태에서, 이 퀸들을 이용해 새 퀸의 자리를 찾아보자
            # 같은 라인에 있거나 대각선에 있으면 배치 불가능
            if queens[j] == i or abs(count - j) == abs(i - queens[j]):
                queen_capable = False
                break
        # 여기까지 왔으면 새 퀸의 자리를 알 수 있다.
        if queen_capable:
            queens[count] = i
            N_Queen(queens, n, count + 1)


N_Queen(QUEENS, N, 0)
print(answer)
