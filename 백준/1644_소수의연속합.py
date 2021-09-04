def solution(n):
    if n == 1:
        return 0
    # N/2 까지의 소수 구하기
    isPrime = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n + 1):
        if isPrime[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                isPrime[j] = False
    print(primes)
    answer = 0
    # N이 소수이면 정답에 추가
    if primes[-1] == n:
        answer += 1
    # 소수의 합 경우의 수 구하기
    s, e = 0, 1
    while s < e < len(primes):
        Sum = sum(primes[s:e])
        if Sum < N:
            e += 1
        elif Sum > N:
            s += 1
        else:
            answer += 1
            primes = primes[s + 1:]
            s, e = 0, 1
    return answer


N = int(input())
print(solution(N))
