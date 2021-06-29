def solution(N):
	if N ==1: return 4
	elif N==2: return 6
	else:
		lst=pibonachi(N)
		return 2*(lst[-1]+lst[-2]*2+lst[-3])

def pibonachi(N):
	lst=[1,1]
	while len(lst)<N:
		lst.append(lst[-1]+lst[-2])
	return lst


print(pibonachi(8))
print(solution(5), solution(6))