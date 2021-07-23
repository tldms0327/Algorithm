def solution(n):
	a,b=0,1
	i=0
	while i<n:
		a,b=b,a+b
		i+=1

	return a%1234567
print(solution(5))

#피보나치 수를 재귀로 구해보려고 했으나
#연산이 두배씩 계속 많아져 시간복잡도가 꽝!