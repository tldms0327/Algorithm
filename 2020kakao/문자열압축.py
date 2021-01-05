# coding=utf-8
# 2020 카카오 블라인드 - 문자열 압축

def solution(s: str) -> int:
    candidate = []
    if len(s) == 1:
        return 1

    for t in range(1, len(s) // 2 + 1):
        # 문자열을 t개씩 잘라서 압축
        subpressed_length = 0
        now_string = ''  # 현재 압축중인 문자열
        now_num = 1  # 압축된 횟수
        for i in range(0, len(s), t):
            next_string = s[i: min(i + t, len(s))]
            # initialize
            if now_string == '':
                now_string = next_string

            elif next_string != now_string:
                # 압축될 수 없는 새로운 문자열이 생겼으니 now status 초기화
                if now_num != 1:
                    # 두 번 이상 압축된 문자열일 때는 (숫자 한글자 + 문자열수)
                    subpressed_length += (t + len(str(now_num)))
                else:
                    # 압축되지 못한 문자열일 때는 문자열 길이만
                    subpressed_length += t
                now_string = next_string
                now_num = 1
            else:
                # 압축 가능할 문자일 때
                now_num += 1
        #             print(i, now_string, now_num, subpressed_length)

        # 마지막 남은 문자열 처리
        if now_num != 1:
            subpressed_length += (t + len(str(now_num)))
        else:
            subpressed_length += len(now_string)
        candidate.append(subpressed_length)

    return min(candidate)

# ========================== pythonic code =============================
def compress(text: str, t: int) -> int:
    words = [text[i:i+t] for i in range(0, len(text), t)]
    res = []
    now_string = words[0]
    now_num = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            now_num += 1
        else:
            res.append([now_string, now_num])
            now_string = b
            now_num = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution2(text: str) -> int:
    return min(compress(text, t) for t in list(range(1, int(len(text)/2) + 1)) + [len(text)])


if __name__ == '__main__':
    print(solution('ababababcdecdecde'), solution2('ababababcdecdecde'))