def solution(arr):
	answer=0
	arr=(arr.replace("()", "*"))
	l = arr.count("*")
	while arr.count("(")>0:
		for i in range(1, l+1):
			searching="("+"*"*i+")"
			while searching in arr:
				temp=arr.replace(searching, "*"*i)
				answer += ((len(arr)-len(temp))/2)*(i+1)
				arr=temp
	return answer

#좀 더 스택에 걸맞는 풀이랄까..
def solution2(arr):
	answer=0
	stick=0
	arr=arr.replace("()", "*")

	for i in arr:
		if i=='(':
			stick+=1
		elif i=='*':
			answer+=stick
		else:
			stick-=1
			answer+=1
	return answer

print(solution2("()(((()())(())()))(())"))
