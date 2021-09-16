def check(place):
    answer = 1
    place = ['OOOOOOO'] + ['O' + p + 'O' for p in place] + ['OOOOOOO']
    print(place)
    for x in range(1, 6):
        for y in range(1, 6):
            if place[x][y] != 'P':
                continue
            # 사람이 앉은 자리에 대해서만 거리두기 확인
            if (x < 4 and place[x + 1][y] == 'O' and place[x + 2][y] == 'P') or (place[x + 1][y] == 'P') or \
                    (y < 4 and place[x][y + 1] == 'O' and place[x][y + 2] == 'P') or (place[x][y + 1] == 'P') or \
                    (place[x + 1][y + 1] == 'P' and (place[x + 1][y] == 'O' or place[x][y + 1] == 'O')) or \
                    (place[x + 1][y - 1] == 'P' and (place[x + 1][y] == 'O' or place[x][y - 1] == 'O')):
                answer = 0
                break

    return answer


def solution(places):
    answer = []
    for p in places:
        answer.append(check(p))
    return answer


P = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(P))
