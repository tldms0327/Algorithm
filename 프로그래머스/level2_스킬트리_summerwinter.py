def solution(skill, trees):
	answer=0
	for x in trees:
		temp=''
		for letter in x:
			if letter in skill:
				temp+=letter
				
		if temp==skill[0:len(temp)]:
			answer+=1
		print(temp, answer)


	return answer


print(solution("CBD", ["BACDE", 'CBADF', 'AECB', 'BDA']))
print('C' in 'CBD')
print('CD' in 'CBD')


#다른 사람 풀이
def solution2(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

print(solution2("CBD", ["BACDE", 'CBADF', 'AECB', 'BDA']))
