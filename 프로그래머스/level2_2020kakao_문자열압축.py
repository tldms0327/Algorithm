def solution(s):
	import copy
	answer=[]
	if len(s)<1:
		return len(s)
	i=1 #i개씩 비교할거
	while i<len(s):
		answer.append(0)
		temp=copy.deepcopy(s)
		one_time=[]
		manytime=[]
		while i<=len(temp):
			word= temp[:i]
			if word not in one_time and word not in manytime:
				one_time.append(word)
				count=1
			elif one_time[-1]!=word:
				one_time.append(word)
				count=1
			elif one_time[-1]==word and word not in manytime:
				count+=1
				manytime.append(word)
			elif word in one_time and word in manytime and word==one_time[-1]:
				count+=1
				if count==10 or count==100 or count==1000:
					print(word)

	

			temp = temp[i:]
		answer[-1] = answer[-1]+(i*len(one_time)+len(manytime)+len(temp))


		i+=1
	return min(answer)

print(solution("aabbaccc"))

print(solution("ababaaaaaaabaaa"))
name = 'a'*10+'b'*100+'c'*10+'d'*100+'a'*100
print(solution(name))


