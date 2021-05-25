def solution(dartResult):
	answer=[]
	for i in range(len(dartResult)):
		if (dartResult[i].isdigit() and dartResult[i]!='0') or i==0:
			answer.append(int(dartResult[i]))
		elif dartResult[i]=='0':
			if dartResult[i-1]=='1':
				answer[-1]==10
			else:
				answer.append(0)

		elif dartResult[i]=='S':
			answer[-1]=answer[-1]**1
		elif dartResult[i]=='D':
			answer[-1]=answer[-1]**2
		elif dartResult[i]=='T':
			answer[-1]=answer[-1]**3
		elif dartResult[i]=='*':
			answer[-1]=answer[-1]*2
			if len(answer)>=2:
				answer[-2]*=2
		elif dartResult[i]=='#':
			answer[-1]=-answer[-1]
	return sum(answer)


a='1S2D*3T'
print(solution(a))

#정규표현식을 이용한 풀이
import re


def solution2(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

print(solution2(a))

print(("-10").isdigit())
print(int("-10"))
a='-10'
if float(a):
	print(float(a))