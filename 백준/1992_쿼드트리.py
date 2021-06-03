import sys


def compressed(grid):
    start = grid[0][0]
    # 모두 같은 수로 이루어져 있으면 그 수를 return
    for line in grid:
        for l in line:
            if l != start:
                return None
    return start


def quadTree(grid):
    answer = "("
    # 이미 압축된 상태면 해당 수만 return
    if compressed(grid):
        return compressed(grid)
    # 4개로 쪼개서 재귀, 출력형식 ()로 맞추기
    else:
        size = len(grid) // 2
        for i in [0, size]:
            for j in [0, size]:
                newGrid = [x[j: j + size] for x in grid[i:i + size]]
                answer += quadTree(newGrid)

    return answer + ")"


n = int(input())
grid = []
for _ in range(n):
    grid.append(sys.stdin.readline().strip())

print(quadTree(grid))
