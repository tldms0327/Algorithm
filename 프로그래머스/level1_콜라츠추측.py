def solution(n):
	count=0
	while n!=1:
		if count>=500:
			return -1
		if n%2==0:
			n=n/2
		else:
			n=n*3+1
		count+=1
	return count

print(solution(626331))