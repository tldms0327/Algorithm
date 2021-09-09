from itertools import combinations


def solution(relation):
    answer = []
    relation_t = [[] for _ in range(len(relation[0]))]
    # 탐색하기 쉽게 relation을 transpose해서 저장해두기
    for r in relation:
        for i, value in enumerate(r):
            relation_t[i].append(value)

    # 키 길이 1인 것부터 완전탐색
    key_length = 1
    while key_length <= len(relation_t):
        possible_key = combinations([i for i in range(len(relation_t))], key_length)
        for key_candidate in possible_key:
            key_candidate = set(key_candidate)
            values = set()
            # 유일성 확인
            for row in relation:
                values.add(tuple([row[k] for k in key_candidate]))

            # 유일성을 만족하는 key일 때
            if len(values) == len(relation):
                # 최소성을 만족하는지 확인
                answer.append(key_candidate)
                for key in answer[:-1]:
                    if key & key_candidate == key:
                        answer.pop()
                        break

        key_length += 1

    return len(answer)


R = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
     ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(R))
