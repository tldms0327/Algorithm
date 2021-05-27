def solution(numbers):
	answer = 0 
	nums = []
	from itertools import permutations as per
	for i in range(1,len(numbers)+1):
		lst = list(map(''.join, per(numbers, i)))
		nums += list(set([int(x) for x in lst if len(str(int(x)))==i and x!= '0' and x!= '1']))


	for num in nums:
		for p in range(2,int(num**0.5)+1):
			if num % p ==0:
				break
		else:
			answer += 1


	return answer


# set의 특징을 잘 살린 코드
def solution2(n):
	from itertools import permutations as per
	answer = set()
	for i in range(len(n)):
		answer |= set(map(int, map("".join, per(list(n), i+1))))
	answer -= set(range(0,2)) # 0,1 제거

	for i in range(2, int(max(answer) ** 0.5)+1): 
		answer -= set(range(i*2, max(answer) +1, i))
	return len(answer)


print(solution2('7843'))