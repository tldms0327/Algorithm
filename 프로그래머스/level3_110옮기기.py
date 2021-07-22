# 000, 001, 010, 011, 100, 101, 110, 111 이므로
# 110이 사전순으로 앞에 오려면 연속된 111 보다 무조건 앞에 있게 하면 된다!
# 해당 문제열에서 110이 나올 때마다 이걸 없애고 110을 다시 탐색하며
# 가능한 모든 경우의 수의 110을 센다
# 연속된 111을 찾아서 그 앞에 110을 넣어준다.

def convert(arr):
    stack = []  # 110을 제외한 문자열 순서대로 담아두기
    cnt_110 = 0
    for i, a in enumerate(arr):
        if len(stack) < 2:
            stack.append(a)
            continue
        if a == '0':
            second = stack.pop()
            first = stack.pop()
            if first + second + a == '110':
                cnt_110 += 1
            else:
                stack.append(first)
                stack.append(second)
                stack.append(a)
        else:
            stack.append(a)

    # print(cnt_110)
    # 110이 없으면 지금이 최상
    if cnt_110 == 0:
        return arr
    # 110을 다 빼버렸으므로 남은 문자열은 10100101.. 이거나 1111...형태밖에 안됨.
    # 따라서 우리는 연속된 1을 찾아야 하는데, 이는 한 군데만 존재할 수밖에 없다
    # print(stack)
    cnt_1 = 0
    if not stack:
        return '110' * cnt_110

    for s in stack[::-1]:
        if s == '0':
            break
        else:
            cnt_1 += 1
    return ''.join(stack[:len(stack) - cnt_1]) + '110' * cnt_110 + '1' * cnt_1


# print(convert('100111100'))


def solution(s):
    answer = []
    for word in s:
        answer.append(convert(word))
    return answer


print(solution(["1110", "100111100", "0111111010"]))


# 좀 더 간결한 풀이 (convert)
def f(x):
    left, I, IIO = '', 0, 0
    for i in x:
        if i == '1':
            I += 1
        elif I > 1:
            I -= 2
            IIO += 1
        else:
            left += '10' if I > 0 else '0'
            I = 0
    return left + '110' * IIO + '1' * I


print(convert('111100011100'))
