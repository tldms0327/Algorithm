def solution(array, commands):
	answer=[]
	for i in range(len(commands)):
		temp = array[commands[i][0]-1:commands[i][1]]
		temp.sort()
		answer.append(temp[commands[i][2]-1])

	return answer


def solution2(array, commands):
#MAP을 쓰면, COMMANDS 요소에 하나씩 접슨해 LAMBDA 합수를 적용하여 그 결과값을
#MAP자료형으로 묶어준다
	return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


print(solution2([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]]))

