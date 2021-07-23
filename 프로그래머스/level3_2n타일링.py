def solution(n):
	a = 1
	b = 1
	for i in range(3, n+2):
		a, b = b, a+b
	return b%1000000007

print(solution(7))


