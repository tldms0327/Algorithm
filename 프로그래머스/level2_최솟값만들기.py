def solution(a,b):
	a.sort()
	b.sort(reverse=True)
	answer=0
	for i in range(len(a)):
		answer+=a[i]*b[i]

	#return sum(x*y for x,y in zip(a,b))
	return answer