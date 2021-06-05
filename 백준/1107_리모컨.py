from itertools import product as p


def solution(ch, buttons):
    size = len(ch)
    ch = int(ch)
    answer = abs(ch - 100)
    if answer == 0:
        return 0
    for i in range(size, 0, -1):
        case = p(buttons, repeat=i)
        for num in case:
            n = int(''.join(list(num)))
            if n == ch and len(str(n)) < answer:
                return i
            elif abs(ch - n) + len(str(n)) < answer:
                answer = abs(ch - n) + len(str(n))

    if '0' in buttons and len(buttons) >= 2:
        n = buttons[1] + '0' * size
        if abs(ch - int(n)) + size + 1 < answer:
            return abs(ch - int(n)) + size + 1
    elif len(buttons) >= 1:
        n = buttons[0] * (size + 1)
        if abs(ch - int(n)) + size + 1 < answer:
            return abs(ch - int(n)) + size + 1

    return answer


target = input()
n = int(input())
if n == 0:
    broken = []
else:
    broken = input().split()
buttons = [str(i) for i in range(10) if str(i) not in broken]
buttons.sort()
print(solution(target, buttons))
