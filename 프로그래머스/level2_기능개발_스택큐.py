def solution(progress, speed):
	import math
	days=[]
	prog_remained=[100-i for i in progress]
	for k in range(len(prog_remained)):
		days.append(math.ceil(prog_remained[k]/speed[k]))

	answer=[]
	i=0
	while i<=len(days)-1:
		count=0
		while days[i]>=days[count+i]:
			count+=1
			if count+i>=len(days):
				break
		answer.append(count)
		
		i+=count

	return answer


print(solution([93,30,55], [1,30,5]))
print(solution([80,79,5,80,95,15], [5,48,9,32,7,8,9]))


def solution2(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

def solution3(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

print(solution3([80,79,5,80,95,15], [5,48,9,32,7,8,9]))


