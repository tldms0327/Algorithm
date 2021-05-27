import heapq #리스트를 최소힙처럼 다룰 수 있게 도와준다.

def solution(scoville, K):
	heapq.heapify(scoville)
	answer=0
	while scoville[0] <K and len(scoville)>1:
		temp = heapq.heappop(scoville)
		
		new = temp + scoville[0]*2
		heapq.heappop(scoville)
		heapq.heappush(scoville, new)
		
		answer+=1


	if len(scoville)==1 and scoville[0]<K:
		return -1

	return answer

print("답:", solution([1,12,2,3,10,9], 7))
print("답:",solution([1,2], 3))
print("답:",solution([1,2,3], 11))
# lst=[1,2,3,4,5]
# print(lst.remove(2))
# print(lst)
# print(lst.pop(2))