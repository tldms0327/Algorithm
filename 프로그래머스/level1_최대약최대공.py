def solution(n,m):
	#최대공약수
	a=1
	for i in range(min(n,m),1,-1):
		if n%i==0 and m%i==0:
			a=i
			break

	j=n*m
	if a!=1:
		while j%n==0 and j%m==0:
			j=j/a
	return [a, int(j*a)]

#유클리드 호제법
#2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), 
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
# 이 성질에 따라, b를 r로 나눈 나머지 r’를 구하고, 
# 다시 r을 r’로 나눈 나머지를 구하는 과정을 반복하여 
# 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다. 
def solution2(n,m):
	a, b = max(n,m), min(n,m)
	t=1
	while t>0:
		t=a%b
		a, b = b, t
	answer = [a, int(n*m/a)]
	return answer

print(solution2(5,36))
