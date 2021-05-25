def solution(n):

	#return sum(map(int, str(n)))
	return sum([int(i) for i in str(n)])
print(solution(123))
print(solution(987))


