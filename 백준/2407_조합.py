from math import factorial as f


def combination(n, m):
    return f(n) // (f(n - m) * f(m))


a, b = map(int, input().split())
print(combination(a, b))
