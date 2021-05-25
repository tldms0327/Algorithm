def solution(n):
	return int(''.join(sorted([i for i in str(n)])[::-1]))

print(solution(118372))