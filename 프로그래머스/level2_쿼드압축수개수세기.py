def solution(arr):
    answer = [0, 0]
    size = len(arr) // 2
    dir = [[0, 0], [0, 1], [1, 0], [1, 1]]

    # 모든 원소가 같은 숫자인지 체크
    total = set()
    for row in arr:
        total = set(row) | total

    # 모두 같은 숫자라면 answer에 추가
    if len(total) == 1:
        answer[total.pop()] += 1
    # 네 개로 쪼개서 재귀 돌리기
    else:
        for d in dir:
            temp_arr = [x[d[1] * size: (d[1] + 1) * size] for x in arr[d[0] * size: (d[0] + 1) * size]]
            temp_answer = solution(temp_arr)
            answer[0] += temp_answer[0]
            answer[1] += temp_answer[1]

    # print(arr, answer)

    return answer

# 예전에 풀었던 것
# def press(x, y, size, arr, answer):
#     # 0으로 압출인지, 1로 압축인지 체크
#     one = True
#     zero = True
#     for i in arr[x: x + size]:
#         for j in i[y: y + size]:
#             if j == 1:
#                 zero = False
#             if j == 0:
#                 one = False
#         # 압축되지 않았을 때
#         if zero == False and one == False:
#             press(x, y, size // 2, arr, answer)
#             press(x, y + size // 2, size // 2, arr, answer)
#             press(x + size // 2, y, size // 2, arr, answer)
#             press(x + size // 2, y + size // 2, size // 2, arr, answer)
#             break
#
#     # 1로 압축됐을 때
#     if one:
#         answer[1] += 1
#     # 0으로 압축됐을 때
#     elif zero:
#         answer[0] += 1
#     # 압축되지 않았을 때
#
#
# # 2
# def solution(arr):
#     answer = [0, 0]
#     press(0, 0, len(arr), arr, answer)
#     return answer
