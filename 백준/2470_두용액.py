from bisect import bisect_left


def findMinSum(plus, minus):
    plus.sort()
    minus.sort()
    candidate = []
    if len(plus) >= 2:
        candidate += [(plus[0] + plus[1], plus[0], plus[1])]
    if len(minus) >= 2:
        candidate += [(minus[0] + minus[1], -minus[1], -minus[0])]
    if plus and minus:
        for m in minus:
            if m <= plus[0]:
                candidate.append((plus[0] - m, -m, plus[0]))
            elif plus[-1] <= m:
                candidate.append((m - plus[-1], -m, plus[-1]))
            else:
                idx = bisect_left(plus, m)
                candidate.append((abs(plus[idx - 1] - m), -m, plus[idx - 1]))
                candidate.append((abs(plus[idx] - m), -m, plus[idx]))

    answer = min(candidate)
    return answer


N = int(input())
p = []
m = []
for n in map(int, input().split()):
    if n >= 0:
        p.append(n)
    else:
        m.append(-n)

ans = findMinSum(p, m)
print(ans[1], ans[2])
