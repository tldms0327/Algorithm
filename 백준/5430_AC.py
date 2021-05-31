import sys
from collections import deque


def solution(func, lst):
    # R이 나오면 숫자만 세서 D의 방향만 설정
    r_cnt = 0
    lst = deque(lst)
    for f in func:
        if f == 'R':
            r_cnt += 1
        else:
            if len(lst) == 0:
                return 'error'
            else:
                if r_cnt % 2 == 0:
                    lst.popleft()
                else:
                    lst.pop()
    lst = list(lst)
    # 마지막에 필요하면 뒤집어주기
    if r_cnt % 2 == 1:
        lst = lst[::-1]

    # 파이썬에서 그냥 리스트를 출력할 시 , 사이에 공백이 저절로 들어가기 때문에
    # 문제에서 요구하는 출력형식을 맞춰준다
    return '[' + ','.join(map(str, lst)) + ']'


i = int(input())
answer = []
for x in range(i):
    func = sys.stdin.readline().strip()
    num = sys.stdin.readline().strip()
    lst = sys.stdin.readline().strip()
    if num == '0':
        answer.append(solution(func, []))
    else:
        operand = list(map(int, lst[1:-1].split(',')))
        answer.append(solution(func, operand))

for a in answer:
    print(a)
