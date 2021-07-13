def solution(s):
    answer = 0
    for i in range(len(s)):
        # 하나씩 옆으로 옮기면서 올바른 괄호인지 체크
        word = s[i:] + s[:i]
        if right_string(word):
            answer += 1

    return answer


def right_string(word):
    # 문자열이 올바른 괄호열인지 체크
    stack = []
    for w in word:
        if w in ['(', '[', '{']:
            stack.append(w)
        elif not stack:
            return False
        else:
            l = stack.pop()
            if l + w not in ['()', '{}', '[]']:
                return False

    if not stack:  # STACK이 비어있으면 올바른 문자열
        return True
    else:
        return False


print(solution("[](){}"))
