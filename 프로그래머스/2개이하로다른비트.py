def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(f2(n))
    return answer


# 시간초과...
def f(num):
    answer = num + 1
    cnt = 0
    while True:
        diff_bit = str(bin(num ^ answer))
        diff_bit = int(diff_bit[2:])
        while diff_bit > 0 and cnt <= 2:
            cnt += diff_bit % 10
            diff_bit //= 10

        if cnt <= 2:
            return answer
        else:
            answer += 1
            cnt = 0


def f2(num):
    # 짝수일 땐 끝자리가 0이므로 1만 더해주면 된다
    if num % 2 == 0:
        return num + 1

    # 홀수일 때 2진수로 바꾼 스트링으로 답을 구해보자
    num = str(bin(num))[2:]
    # 주어진 수에 0이 하나도 없다면(1111) 맨 앞에 1을 더해줄 수밖에 없음
    if num.count('0') == 0:
        num = '10' + num[1:] # 10111
    # 0이 있어서 비트를 바꿀 수 있을 땐 가장 작은 자리수의 0을 1로 바꾸고,
    # 그 0 오른쪽에 1이 있다면 0으로 바꿔주자
    else:
        for i, n in enumerate(num[::-1]):
            if n == '0':
                if i == 1:
                    num = num[:-1 * i - 1] + '10'
                else:
                    num = num[:-1 * i - 1] + '10' + num[-1 * i+1:]

                break
    return int(num, 2)


# print(solution([343, 254, 779, 421]))
# 347 1019 781  446
print(solution([1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]
))
