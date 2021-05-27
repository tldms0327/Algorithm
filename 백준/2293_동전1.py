from itertools import product as pro
import sys
 


def solution(n, k, lst):
    case = []
    answer = [0 for x in range(k+1)]
    answer[0] = 1
    
    for i in lst:
        for j in range(i, k+1):
            answer[j] += answer[j-i]
            
    return answer[k]

# print(solution(3, 10, [1,2,5]))


n, k = list(map(int, sys.stdin.readline().split()))
lst = []
for i in range(n):
    temp = int(sys.stdin.readline())
    lst.append(temp)

print(solution(n, k, lst))