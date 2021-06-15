def solution(N, stages):
	fail = []
	failrate=[]
	for i in range(1,N+2):
		fail.append(stages.count(i))
		
	for i in range(N):
		if sum([x for x in fail[i:]])==0:
			failrate.append(0)
		else:
			failrate.append(fail[i]/sum([x for x in fail[i:]]))

	answer={}
	for i in range(N):
		answer[i+1]=failrate[i]
	

	return [x[0] for x in sorted(answer.items(), key=(lambda x: -x[1]))]

print(solution(5,[2,1,2,4,2,4,3,3]))
print(solution(4,[4,4,4,4,4,4]))

#쪼꼼 더 간결하게
def solution2(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
