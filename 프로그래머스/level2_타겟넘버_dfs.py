def solution(num, target):
	answer=[num[0], -num[0]]
	i=2
	for j in num[1:]:
		for k in range(i):
			answer.append(answer[k]+j)
			answer.append(answer[k]-j)
		answer=answer[i:]
		i=i*2

	#시간복잡도: 2^n
	return answer.count(target)
 #itertools
from itertools import product, permutations
def solution2(num, target):
 	l = [(x,-x) for x in num]
 	print(l, *l)
 	print(list(product(*l)))

 	s= list(map(sum, product(*l)))
 	return s.count(target)


print(solution2([1,1,1,1,1], 3))
#product: 중첩된 for loop 에 해당하는 데카르트의 곱
#permutations: 길이 r 만큼 가능한 모든 순서, 반복 없음
print(list(product('ABCD')),'\n', list(product('abcd', repeat=3)))
print(list(product()))
print(list(permutations('ABCD',2)),'\n', list(permutations('abcd', 3)))

#재귀를 이용한 방법!!
def solution3(num, target):
	if not num and target==0:
		return 1
	elif not numbers:
		return 0
	else:
		return solution(numbers[1:], target-numbers[0])\
		+solution(numbers[1:], target+number[0])


