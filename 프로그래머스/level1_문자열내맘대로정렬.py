def solution(strings, n):
	lst=[]
	answer=[]
	for word in strings:
		lst.append([word[n],word])
	lst.sort()
	for idx in lst:
		answer.append(idx[1])

	return answer
dic={'u':'sun', 'e':['aed','bed'], 'a':'car'}


print(solution(['sun', 'bed', 'car', 'tune'], 1))

#다른풀이-sorted 사용 
#sorted 모듈은 jupyter에 따로 정리! 
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])