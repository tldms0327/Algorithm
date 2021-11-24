def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    dp = [[0 for _ in range(m)] for __ in range(n)]
    for s in skill:
        type, r1, c1, r2, c2, degree = s
        if type == 1:
            degree = -degree
        # dp[r1][c1] += degree
        # dp[r2][c2] -= degree
        for r in range(r1, r2 + 1):
            if c2+1  < m:
                dp[r][c1 + 1] += degree
                dp[r][c2 + 1] -= degree
        print(dp)
    print(dp)
    for r, row in enumerate(board):
        print(row, dp[r])
        row[0] += dp[r][0]
        for i in range(1, m):
            row[i] = row[i - 1] + dp[r][i]
        print(row)

    print(board)

    for row in board:
        for x in row:
            if x > 0:
                answer += 1

    return answer


B = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
S = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
print(solution(B, S))
