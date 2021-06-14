def solution2(number, k): # permutation은 시간복잡도가 너무 별로ㅠㅠ 시간 초과!
	import itertools as it
	lst = sorted(list(map(int,map(''.join, it.permutations(number, len(number)-k)))), reverse=True)

	answer = 0
	for x in lst:
		temp = []
		t = -1
		for s in str(x):
			t = number.find(s, t+1)
			if t ==-1:
				break
			else:
				continue
		if t == -1:
			continue
		else:
			answer = str(x)
			break

	return answer
	# return "".join(x for x in sorted(number, reverse=True)[:-2])

def solution(number, k):
	n = len(number) - k
	answer =""
	t = -1
	while n > 0:
		left = list(number[t+1:len(number)-n+1])
		right = number[len(number)-n+1:]
		print('left:', left, 'right:', right)
		l_big = max([int(x) for x in left])
		t = left.index(str(l_big))
		n -= 1
		answer += str(l_big)
		print('n:', n, 'answer:', answer, 't:', t, 'l_big:', l_big)



	return answer
k = "1924"
m= [1,2,3,4]
m=m.pop(0)
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("87654321",3))
print(solution("1111111", 3))


#print(solution("4177252841", 4))
num = '01'
print(k[int(num[0])+1:int(num[1])],k[int(num[1])+1:])
