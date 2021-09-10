from itertools import permutations


def solution(expression):
    answer = 0
    # 가능한 우선순위 조합 뽑기
    operators = list(permutations([x for x in ['-', '+', '*'] if x in expression]))
    expressions = []
    number = ''
    # 주어진 문자열을 숫자와 연산자로 분리
    for letter in expression:
        if letter.isalnum():
            number += letter
        else:
            expressions.append(int(number))
            expressions.append(letter)
            number = ''
    expressions.append(int(number))
    # 스택을 이용하여 각 경우의 수를 계산, 가장 큰 수 찾기
    for operator in list(operators):
        stack = []
        temp = expressions[:]
        for op in operator:
            for i, e in enumerate(temp):
                if e != op:
                    stack.append(e)
                else:
                    x = stack.pop()
                    if op == '+':
                        temp[i + 1] = x + temp[i + 1]
                    elif op == '-':
                        temp[i + 1] = x - temp[i + 1]
                    else:
                        temp[i + 1] = x * temp[i + 1]
            temp, stack = stack[:], []
        answer = max(answer, abs((temp[0])))

    return answer


print(solution("100-200*300-500+20"))
