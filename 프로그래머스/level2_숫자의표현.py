def solution(n):
	answer=0
	summ=0
	count=1
	while summ+count <=n:
		summ+=count
		if (n-summ)%count==0:
			answer+=1

		count+=1

	return answer
print(solution(15))