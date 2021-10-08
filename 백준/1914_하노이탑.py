import sys

sys.setrecursionlimit(1000000)


def hanoi_top(n, dep, dest):
    global answer
    another = [x for x in range(1, 4) if x not in [dep, dest]][0]

    if n == 1:
        answer += [[dep, dest]]

    else:
        hanoi_top(n - 1, dep, another)
        answer += [[dep, dest]]
        hanoi_top(n - 1, another, dest)
        return answer


answer = []
n = int(input())
if n > 20:
    print(2 ** n - 1)
else:
    hanoi_top(n, 1, 3)
    print(len(answer))
    for r in answer:
        print(r[0], r[1])
