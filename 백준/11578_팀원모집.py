from collections import OrderedDict
from itertools import combinations as C

n, m = map(int, input().split())
student_info = {i: {} for i in range(m)}
for i in range(m):
    inputs = list(map(int, input().strip().split()))
    student_info[i] = set(inputs[1:])

k = 0
solved = False
while k < m and not solved:
    k += 1
    candidates = C(range(m), k)
    for people in candidates:
        temp = set()
        for p in people:
            temp |= student_info[p]
        if len(temp) == n:
            solved = True
            break

if solved:
    print(k)
else:
    print(-1)
