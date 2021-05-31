# 헉 모범답안이랑 똑같아 ㅎㅎㅎ

def solution(s):
	stack=[]
	for cha in s:
		if not stack:
			stack.append(cha)
		else:
			if stack[-1]==cha:
				stack.pop()
			else:
				stack.append(cha)

	return int(len(stack)==0)  # not(stack)


print(solution('baabaa'))
