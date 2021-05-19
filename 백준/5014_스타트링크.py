import sys


def solution(f, s, g, u, d):
    answer = 0
    # f: 전체층, s: start, g: dest., u: up, d: down
    floor = [0 for _ in range(f + 1)]
    floor[s] = 1
    visited, new_visited = set(), set()
    visited.add(s)

    while floor[g] == 0:
        answer += 1
        # 이번 iter에서 새로 방문한 층
        for v in visited:
            # 여기서 floor의 인덱스로 안 찾고 visited에서 원소찾기(not in)하면 시간초과!!
            if v + u <= f and floor[v + u] == 0:
                new_visited.add(v + u)
                floor[v + u] = 1
            if v - d > 0 and floor[v - d] == 0:
                new_visited.add(v - d)
                floor[v - d] = 1

        # 새로운 층이 더 이상 없으면 실패
        if not new_visited and floor[g] == 0:
            return "use the stairs"
        else:
            visited = new_visited
            new_visited = set()

    return str(answer)


a, b, c, d, e = list(map(int, sys.stdin.readline().split()))
print(solution(a, b, c, d, e))
