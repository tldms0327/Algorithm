import sys


def solution(numbers):
    trie = dict()
    answer = True
    for number in numbers:
        if not answer:
            break
        cur_node = trie
        for s in number:
            if s not in cur_node:
                cur_node[s] = dict()
            else:
                if len(cur_node[s]) == 0:
                    answer = False
                    break
            cur_node = cur_node[s]
        if len(cur_node) > 0:
            answer = False

    return answer


N = int(input())
answers = []
for _ in range(N):
    C = int(input())
    lst = []
    for _ in range(C):
        lst.append(sys.stdin.readline().strip())
    if solution(lst):
        answers.append("YES")
    else:
        answers.append("NO")
print('\n'.join(answers))
