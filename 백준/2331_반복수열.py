import sys


def solution(n, p):
    series = dict()
    series[n] = 0
    # 현재 시리즈 안의 마지막 원소로 만드는 다음 수
    nextNum = newNumCal(n, p)
    idx = 1

    # 반복되는 부분의 시작 찾기
    while nextNum not in series:
        series[nextNum] = idx
        nextNum = newNumCal(nextNum, p)
        idx += 1

    # -> nextNum은 처음 반복의 시작이 되는 수

    return series[nextNum]


def newNumCal(num, p):
    return sum([int(i) ** p for i in str(num)])


N, P = list(map(int, sys.stdin.readline().split()))
print(solution(N, P))
