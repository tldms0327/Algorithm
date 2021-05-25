def solution(s):
	p=0
	y=0
	letter = list(s.lower())
	for idx, l in enumerate(sorted(letter)):
		if l=='p':
			p+=1
		elif l=='y':
			y+=1
	return p==y


#다른사람 풀이
#count() 집계함수 이용
def countPY(s):
	return s.lower().count('p') == s.lower().count('y')

#Counter 이용
from collections import Counter
def CounterPY(s):
	c = Counter(s.lower())
	return c['y']== c['p']

print(solution("pPoooyY"))
print(countPY("pPoooyY"))
print(CounterPY("pPoooyY"))