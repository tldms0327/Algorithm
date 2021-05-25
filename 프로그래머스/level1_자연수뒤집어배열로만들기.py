#오 한번에 풀었당><
def solution(n):
	#내 풀이
	return [int(i) for i in str(n)][::-1]
	#다른사람 풀이: map 사용
	return list(map(int, reversed(str(n))))

print(solution(12345))
