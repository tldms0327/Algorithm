def solution(numbers):
	number= [str(x) for x in numbers]
	answer = "".join(sorted(number, key=lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]), reverse=True))
	return answer if int(answer) !=0 else "0"



print(solution([1,2,3,4]))
print(solution([6,10,2]))
print(solution([3,30,34,5,9]))
print('5'<'8', '44'<'7')