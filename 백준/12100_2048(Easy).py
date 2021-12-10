from itertools import product


def move(board, size, direction):
    """size N인 게임판을 direction방향으로 한 번 움직이고 난 후의 게임판
    direction: 1: top, 2: bottom, 3: left, 4: right"""
    new_board = [[] for _ in range(size)]
    if direction == 0:
        for i in range(size):
            arr = push_sum([board[j][i] for j in range(size)], size)
            for j in range(size):
                new_board[j].append(arr[j])
    elif direction == 1:
        for i in range(size):
            arr = push_sum([board[j][i] for j in range(size)][::-1], size)
            for j in range(size):
                new_board[j].append(arr[-j - 1])
    elif direction == 2:
        for i in range(size):
            arr = push_sum(board[i], size)
            new_board[i] = arr
    elif direction == 3:
        for i in range(size):
            arr = push_sum(board[i][::-1], size)
            new_board[i] = arr[::-1]

    return new_board


def push_sum(arr, size):
    new_arr = []
    for a in arr:
        if a == 0:
            continue
        elif new_arr and new_arr[-1][0] == a and not new_arr[-1][1]:
            b, flag = new_arr.pop()
            new_arr.append([a + b, True])
        else:
            new_arr.append([a, False])

    return [x[0] for x in new_arr] + [0 for _ in range(size - len(new_arr))]


N = int(input())
Board = []
for _ in range(N):
    Board.append(list(map(int, input().split())))

answer = 0
all_cases = product(range(4), range(4), range(4), range(4), range(4))
for case in all_cases:
    board = Board[:]
    for dirr in case:
        board = move(board, N, dirr)
    answer = max(answer, max([max(l) for l in board]))

print(answer)
