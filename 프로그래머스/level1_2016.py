def solution(a,b):
	answer = ['THU','FRI', 'SAT','SUN', 'MON', 'TUE', 'WED']
	month = [3,1,3,2,3,2,3,3,2,3,2,3]
	i=1
	total=0
	while i<=(a-1):
		total+=month[i-1]
		i+=1
	total+=b
	#한 줄로 표현하기
	# return answer[(sum(month[:a-1])+b)%7]
	return answer[total%7]

#함수 활용하기
import datetime

def solution2(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]

print(solution(5,24))
print(solution2(5,24))


