a, b = map(int, input().split())

answer = 1
visited = [a]
i = 0

while b not in visited:
    answer += 1
    temp = []
    for n in visited:
        if n * 2 > b:
            continue
        elif n * 10 + 1 > b:
            temp.append(n * 2)
        else:
            temp.append(n * 2)
            temp.append(n * 10 + 1)

    if not temp or min(temp) > b:
        answer = -1
        break
    visited = temp[:]


print(answer)
