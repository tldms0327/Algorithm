def solution(answers):
    c1, c2, c3 = 0,0,0
    answer=[]
    for i in range(0, len(answers)):
        if answers[i]== [1,2,3,4,5][i%5]: 
            c1+=1
        if answers[i]==[2,1,2,3,2,4,2,5][i%8]:
            c2+=1
        if answers[i]==[3,3,1,1,2,2,4,4,5,5][i%10]:
            c3+=1

    
    for j in range(0,3):
        if [c1,c2,c3][j]==max(c1,c2,c3):
            answer.append(j+1)


    return answer


print(solution([1,3,2,4,2]))
print(solution([1,2,3,4,5]))


#cycle을 이용한 코드
from itertools import cycle

def solution3(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]
