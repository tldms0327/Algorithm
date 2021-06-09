def solution(n, s):
    size = 2 * n + 1
    answer = 0

    stack = 0
    for i, x in enumerate(s):
        if not stack:
            if x == 'I':
                stack += 1
        else:
            # 다른 문자열이면 count하고 패스
            if x != s[i - 1]:
                stack += 1
            # 같으면 p 세고 초기화
            else:
                if stack >= size:
                    answer += (stack - size) // 2 + 1
                if x == 'I':
                    stack = 1
                else:
                    stack = 0

    if stack >= size:
        answer += (stack - size) // 2 + 1

    return answer


N = int(input())
_ = input()
print(solution(N, input()))
