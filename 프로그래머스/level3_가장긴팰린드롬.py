def solution(s):
    answer = 1
    size = len(s)
    if size == 2 and s[0] == s[1]:
        return 2
    for i in range(1, size - 1):
        answer = max(answer, palindrome(i, s, size))

    return answer


def palindrome(x, s, size):
    # x라는 기준점에서 양옆으로 뻗어나가며 팰린드롬 문자열의 개수를 센다

    nums = [1]
    # 짝수 팰린드롬 세기
    if s[x] == s[x - 1]:
        num = 2
        start, end = x - 2, x + 1
        while start >= 0 and 0 < end < size:
            if s[start] == s[end]:
                num += 2
                start -= 1
                end += 1
            else:
                break
        nums.append(num)
    # 홀수 팰린드롬 세기
    if s[x - 1] == s[x + 1]:
        num = 1
        start, end = x - 1, x + 1
        while start >= 0 and 0 < end < size:
            if s[start] == s[end]:
                num += 2
                start -= 1
                end += 1
            else:
                break
        nums.append(num)

    return max(nums)


print(solution("abaabaaaaaaa"))
