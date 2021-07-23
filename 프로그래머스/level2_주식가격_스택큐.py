def solution(prices):
	answer=[]
	for i in range(len(prices)-1):
		for j in range(i+1,len(prices)):
			t=len(prices)-1-i
			if prices[j]<prices[i]:
				t=j-i
				break

		answer.append(t)
	answer.append(0)

	return answer

print(solution([1,2,3,2,3]))
