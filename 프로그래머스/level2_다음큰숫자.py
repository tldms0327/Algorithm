def solution(n):
	x = binary_ones(n)
	n+=1
	answer=binary_ones(n)
	while x!=answer:
		n+=1
		answer=binary_ones(n)
	return n

def binary_ones(n):
	count=0
	while n>0:
		count+=n%2
		n=n//2
	return count

#2진수로 알아서 바꿔주는 함수가 있었네...
def nextBigNumber(n):
    answer = n

    while True:
        answer += 1
        if str(bin(answer)).count('1') == str(bin(n)).count('1'):
            return answer


print(solution(13))
print(solution(78))
print(solution(30))


