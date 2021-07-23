def solution(s):
	lst=[int(x) for x in s.split(" ")]
	return str(min(lst))+" "+str(max(lst))

print(solution("1 2 3 4"))
print(solution("-1 -1"))