from collections import defaultdict


def solution(gems):
    n = len(set(gems))
    gem_set = set()
    gem_count = defaultdict(int)
    i = -1
    # 맨 처음부터 시작해서 모든 보석을 시작하는 지점 찾기
    while len(gem_set) != n:
        i += 1
        gem_set.add(gems[i])
        gem_count[gems[i]] += 1
    answer = [[i - 0, 0, i]]

    start, end = 0, i
    while len(gems) > end > start:
        start_gem = gems[start]
        if gem_count[start_gem] > 1:
            start += 1
            gem_count[start_gem] -= 1
        # start 를 왼쪽으로 옮기면 보석 종류가 줄어드는 경우(end를 오른쪽으로 연장해야 하는 경우)
        else:
            # end 를 오른쪽으로 연장하면 보석 종류를 유지할 수 있을 때
            if start_gem in gems[end:]:
                # 빠진 보석을 오른쪽에서 찾으면서 보석 세기
                for i, gem in enumerate(gems[end:]):
                    if i == 0:
                        continue
                    gem_count[gem] += 1
                    if gem == start_gem:
                        gem_count[gem] -= 1
                        break
                start += 1
                end += i
            # end 오른쪽에 start_gem이 없어서 더 이상 탐색할 필요가 없을 때
            else:
                break
        answer.append([end - start, start, end])

    answer = sorted(answer)
    return [answer[0][1] + 1, answer[0][2] + 1]


g = ['DIA', 'EM', 'EM', 'RUB', 'DIA']
print(solution(g))
