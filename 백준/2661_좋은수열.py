n = int(input())

answer = '1'
visited = [[False, False, False] for _ in range(n + 1)]


def isGoodArray(arr, size):
    # 문자열이 좋은수열에 해당하는지 체크
    possible = True
    for s in range(1, size // 2 + 1):
        if arr[size - s:] == arr[size - s * 2:size - s]:
            possible = False
            break
    return possible


def backTracking(size):
    global visited, answer
    # 원하는 길이의 좋은 수열이 나올 때까지 탐색
    while len(answer) < size:
        target_size = len(answer) + 1
        # 1, 2, 3 순서대로 탐색하면 가장 작은 수를 찾을 수 있음
        for i in range(3):
            if not visited[target_size][i] and isGoodArray(answer + str(i + 1), target_size):
                answer += str(i + 1)
                visited[target_size][i] = True
                break
        # answer가 그대로면 더 앞으로 되돌아가서 다시 탐색
        if len(answer) != target_size:
            answer = answer[:-1]


backTracking(n)
print(answer)
