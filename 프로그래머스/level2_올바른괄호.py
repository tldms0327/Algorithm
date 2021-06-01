def solution(s):
	temp=[]
	for x in s:
		if x=="(":
			temp.append(x)
		else:
			if not temp or temp[-1]!='(':
				return False
			else:
				temp.pop(-1)
	if len(temp)!=0:
		return False

	return True

print(solution("()())"))