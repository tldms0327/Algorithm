from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    reporting_user = defaultdict(set)
    count_report = defaultdict(set)
    stopped_user = set()
    for r in report:
        x, y = r.split(" ")
        reporting_user[x].add(y)
        count_report[y].add(x)

    for user in count_report:
        if len(count_report[user]) >= k:
            stopped_user.add(user)
    for id in id_list:
        answer.append(len(reporting_user[id] & stopped_user))

    return answer


I = ["muzi", "frodo", "apeach", "neo"]
R = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
K = 2
print(solution(I, R, K))
