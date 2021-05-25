def solution(board, moves):
	answer=0
	result=[]
	N=len(board)
	for move in moves:
		i=0
		
		while i<=N-1 and board[i][move-1]==0 :
			i+=1

		if i!=N:
			result.append(board[i][move-1])
			board[i][move-1]=0
			if len(result)>=2 and result[-1]==result[-2]:
				result= result[:-2]
				answer+=2



	return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],\
	[1,5,3,5,1,2,1,4]))