import sys


def solution(size, nums):
    stack = [0]
    i = 0
    answer = ['-1' for _ in range(size)]
    while stack and i < size:
        while stack and nums[i] > nums[stack[-1]]:
            answer[stack[-1]] = str(nums[i])
            stack.pop()
        stack.append(i)
        i += 1

    return answer


k = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

print(' '.join(solution(k, lst)))
