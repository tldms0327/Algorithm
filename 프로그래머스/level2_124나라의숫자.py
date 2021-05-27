def solution(n):
	n-=1
	num='124'
	idx=[]
	i=1
	answer=''
	while n>=0:
		idx.append(n%(3**i))
		n=n-3**i-n%(3**i)
		i+=1

	for i, x in enumerate(idx):
		answer=num[(x//(3**i))]+answer


	
	return answer

for i in range(12):
	print(i,solution(i))

#다른사람 풀이.. 나도 심플하게 풀고싶다ㅠ
def solution2(n):
	num=['1', '2', '4']
	answer=''

	while n>0:
		n-=1
		answer = num[n%3]+answer
		n//=3
	return answer


#재귀함수 써서 한번 해보자!
def solution3(n):
	num='124'
	if n<=3:
		return num[n-1]
	else:
		return solution3((n-1)//3)+num[(n-1)%3]


	

for i in range(12):
	print(i,solution3(i))