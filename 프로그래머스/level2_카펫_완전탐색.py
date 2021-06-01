def solution(brown, red):
	answer=[]
	brown=int((brown-4)/2)
	for i in range(1, int(brown/2)+2):
		
		if red/(brown-i)==i :
			answer=[i+2, brown-i+2]
			break
		else:
			i+=1

	return sorted(answer)

print(solution(24,24))