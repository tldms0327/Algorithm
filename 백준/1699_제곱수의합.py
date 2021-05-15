import sys


x = int(sys.stdin.readline())
global lst
lst = [0 for _ in range(x+1)]
lst[1] = 1
nums = []  # k보다 작은 제곱수들
for i in range(int(x ** 0.5), 0, -1):
    nums.append(i ** 2)
    lst[i ** 2] = 1


def solution(k, primes):
    if lst[k] != 0:
        return lst[k]

    answer = []
    for idx, n in enumerate(primes):
        # print(k, n, lst)
        if k - n == 1:
            answer.append(2)
        elif lst[k - n] != 0:
            answer.append(1 + lst[k - n])
        elif k - n in nums:
            lst[k] = 2
            return 2
        elif lst[k - n] == 0:
            answer.append(solution(k - n, [x for x in primes if x <= k - n]) + 1)
    answer = min(answer)
    lst[k] = answer
    return answer


solution(x, nums)
print(lst[-1])
