def solution(clothes):

	kind={}
	for x in clothes:
		if x[1] not in kind:
			kind[x[1]]=1
		else:
			kind[x[1]]+=1

	answer=1
	for key in kind:
		answer=answer*(kind[key]+1)
	return answer-1

print(solution([['yellow_hat', 'headgear'], 
	['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))

#collection
from collections import Counter
from functools import reduce
def solution2(c):
	return reduce(lambda x,y: x*y, [a+1 for a in Counter([x[1] for x in c]).values()])-1

print((solution2([['yellow_hat', 'headgear'], 
	['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])))