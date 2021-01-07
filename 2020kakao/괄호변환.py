# coding=utf-8
def solution(text):
    if if_correct(text):
        return text
    u, v = seperate(text)

    if if_correct(u):
        # u가 올바른 괄호 문자열이라면 문자열 v에 대해 재귀적으로 수행한다.
        answer = u + solution(v)
    else:
        # u가 올바른 괄호 문자열이 아니라면
        # v에 대해 재귀적으로 수행한 결과 앞뒤에 ()를 붙인다.
        temp = '(' + solution(v) + ')'
        # u의 첫 번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향을 뒤집어 붙인다.
        converted_u = ''
        for _ in u[1:-1]:
            if _ == '(':
                converted_u += ')'
            else:
                converted_u += '('
        # 두 문자열을 input text에 대한 답이 된다.
        return temp + converted_u
    return answer


def seperate(text):
    """ 문자열을 균형잡힌 괄호 문자열 u, v로 분리.
        u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없다."""
    left = 0
    right = 0
    for i, t in enumerate(text):
        if t == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return text[:i + 1], text[i + 1:]
        else:
            continue
    return text, ''


def if_correct(text):
    """문자열이 균형잡힌, 올바른 문자열인지 판단. stack 구조 이용."""
    #     print('u', text)
    if text == '':
        return True
    stack = [text[0]]
    for t in text[1:]:
        if t == '(':
            stack.append(t)
        elif t == ')' and stack:
            stack.pop()
        else:
            return False
    if stack:
        return False
    else:
        return True


print(solution('(())(())'))
print(solution(')((()))()('))
