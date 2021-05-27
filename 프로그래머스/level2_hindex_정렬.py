def solution(citations):
	answer=0
	citations.sort()
	for h in range(len(citations), 1,-1):
		if len([i for i in citations if i>=h])>=h:
			answer=h
			break
	return answer
	

print(solution([3,0,6,1,5]))
print(solution([4,3,3,3,3]))

def solution2(citations):
	citations.sort()
	for i in range(len(citations)):
		if citations[i]>=l-i:
			return l-i
	return 0


#개쩐당 호호호
def solution3(citations):
	citations.sort(reverse=True)
	return max(map(min, enumerate(citations, start=1)))






lst=[6,5,3,1,0]
print(list(map(min,enumerate(lst, start=1))))
for idx, s in enumerate(lst, start=1):
	print(idx,s)
	print(min(idx, s))

print(solution3([3,0,6,1,5]))
print(solution3([4,3,3,3,3]))