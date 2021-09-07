def solution(word):
    answer = 0
    lst = ['A', 'E', 'I', 'O', 'U']
    nums = [781, 156, 31, 6, 1]
    for i, s in enumerate(word):
        answer += nums[i] * lst.index(s)
    answer += len(word)
    return answer


print(solution('AAAAE'))
# Axxxx 개수
# 1 + 5 + 25 + 125 + 625 = 750 + 41 = 781
# 781, 156, 31, 6, 1
# 781 * 2 = 1562
# EIO = 781 + 3 + 4 + 6 + 6 = 800
