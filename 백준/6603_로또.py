from itertools import combinations as com
import sys


def solution(arr):
    answer = ''

    combi = com(arr, 6)
    for c in combi:
        answer += " ".join(map(str, c)) + "\n"
    return answer + "\n"


output = ''
while True:
    line = sys.stdin.readline().split()
    size = line[0]
    if size == '0':
        break
    else:
        output += solution(line[1:])

print(output)