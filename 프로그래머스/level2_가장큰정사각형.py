#틀렸네....
def solution2(board):
	import numpy as np

	try:
		row = [sum(x) for x in board]
		col = [sum(x) for x in np.transpose(board)]
		x = min(len(row), len(col))
	except:
		return 1
	

	return min(max_length(row, x), max_length(col, x))**2


def max_length(lst, length):
	for x in range(length, -1,-1):
		if '1'*x in "".join([str(k) for k in [int(i>=x) for i in lst]]):
			count=x
			break
	return count


# 다시 보자...
def solution(board):
    length=0
    flag = False
    map = [rv for rv in board]

    for ri,rv in enumerate(board):
        for ci,cv in enumerate(rv):
            if ri==0 or ci==0 :
                if board[ri][ci]==1:
                    length = max(length,1)
                continue            
            minimum = min(map[ri-1][ci],map[ri][ci-1])
            minimum = min(minimum,map[ri-1][ci-1])

            if board[ri][ci]==1:
                map[ri][ci]= minimum+1
                length = max(length,map[ri][ci])

    answer = length*length

    return answer

def solution3(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j]==1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    return max([col for row in board for col in row])**2





# print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
# print(solution([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]))
# print(solution([[0,0,1,1],[1,1,1,1]]))
# print(solution([0,0,1,1]))

