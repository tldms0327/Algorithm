def solution(heights):
	h=heights[::-1]
	answer=[0 for i in range(len(heights))] #[0]*len(h)
	for idx, height in enumerate(h):
		for j in range(idx+1, len(h)):
			if h[j]>h[idx]:
				answer[idx]=len(h)-j
				break

	return answer[::-1]

print(solution([6,9,5,7,4]))
print(solution([3,9,9,3,5,7,2]))

#range는 역순도 가능하징
def solution2(h):
	answer=[0]*len(h)
	for i in range(len(h)-1, 0, -1):
		for j in range(i-1, -1, -1):
			if h[i] <h[j]:
				answer[i]= j+1
				break
	return answer

#stack의 개념을 이용한 풀이
def solution3(heights):
    answer = []
    # 1. 스택 생성
    st = []
    
    # 2. heights 계산
    while heights:
        # 1. 맨 뒤 송신탑 꺼내옴.
        top = heights.pop()
        
        # 2. 현재 송신탑보다, 큰 송신탑이 나타날때까지 스택에 저장.
        while heights and heights[-1] <= top:
            st.append(heights.pop())
        
        # 3. 남아있는 길이를 asnwer에 저장
        answer.append(len(heights))
        
        # 4. 스택에 저장된 송신탑들을 다시 heights로 돌림
        while st:
            heights.append(st.pop())
    
    # 3. answer 역순으로 변환
    answer = answer[::-1]
    return answer

print(solution3([6,9,5,7,4]))
print(solution3([3,9,9,3,5,7,2]))

lst=[1,2,3,4,5]

while lst:
	print(lst.pop())
print(lst)    