N = int(input())
graph = dict()

for person in range(N):
    friends = input()

    # 한 사람의 친구 목록을 set로 받는다.
    graph[person] = set()
    for i, f in enumerate(friends):
        if f == "N":
            continue
        else:
            graph[person].add(i)


def mostFamousPerson(n, graph):
    answer = 0

    for p in graph:
        # 한 사람의 친구 목록 초기화
        friend = set() | graph[p]

        # 친구의 친구들을 내 친구에 포함시키기
        for f in list(graph[p]):
            friend = friend | graph[f]
        # '나'는 친구가 아니므로 모든 친구에서 1 빼기
        answer = max(answer, len(friend) - 1)

    return answer


print(mostFamousPerson(N, graph))
