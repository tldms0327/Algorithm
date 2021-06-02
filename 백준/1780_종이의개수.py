import sys


# 종이가 모두 같은 수인가?
def same_numbers(p):
    i = p[0][0]
    for arr in p:
        # 한 줄에 다 같은 수로 돼 있지 않거나, 첫번재 숫자와 다른 숫자로 이루어진 경우
        if len(set(arr)) != 1 or i not in set(arr):
            return False
    return True


# 9개의 종이로 쪼개기
def split_paper(p):
    n = int(len(p) / 3)
    seperated = []
    for i in range(3):
        for j in range(3):
            seperated.append([row[j * n:(j + 1) * n] for row in p[i * n: (i + 1) * n]])

    return seperated


size = int(input())
paper = []  # 처음 종이
for s in range(size):
    paper.append(list(map(int, sys.stdin.readline().split())))

papers = [paper]  # 찢어봐야 할 종이들
answer = {0: 0, 1: 0, -1: 0}
while papers:
    paper = papers.pop()
    if not same_numbers(paper):
        papers += split_paper(paper)
    else:
        answer[paper[0][0]] += 1

print(answer[-1], answer[0], answer[1], sep='\n')
