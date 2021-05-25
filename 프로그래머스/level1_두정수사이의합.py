def solution(a,b):
	if a==b:
		return a
	else:
		answer=[a,b]
		answer.sort()
		i=answer[0]
		while i<(answer[1]-1):
			answer.append(i+1)
			i+=1
		return sum(answer)


#더 빠른 풀이...
def solution2(a,b):
	if a==b:
		return a
	elif a>b:
		a,b = b,a
	return(sum(range(a,b+1)))



print(solution2(3,5))