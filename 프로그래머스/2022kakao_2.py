def solution(n, k):
    answer = 0
    num = converter(n, k)
    num = num.strip().split('0')
    for n in num:
        if len(n) >= 1 and n != '1' and '0' not in n and n.isdigit():
            if prime_number(int(n)):
                answer += 1

    return answer


def converter(n, k):
    result = ''
    while n > 0:
        result += str(n % k)
        n //= k
    return result[::-1]


def prime_number(n):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    return is_prime


print(converter(7777, 10))
print(solution(1000000, 4))
print(prime_number(121221))
