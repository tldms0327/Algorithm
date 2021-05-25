def solution(participant, completion):
    if len(participant)==1:
        answer= participant[0]
    else:
        answer=''
        participant.sort()
        completion.sort()
        for i in range(len(completion)):
            if participant[i]!= completion[i]:
                answer= participant[i]
                break
    
        if answer=='':
            answer= participant[-1]

        return answer

#collections이용
import collections
def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


#hash값은 key가 다르면 모두 다르다는 특징을 살린 코드
def solution_hash(participant, completion):
    answer=''
    temp =0
    dic ={}
    for part in participant:
        dic[hash(part)] = part
        temp +=int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

#zip 
def solution3(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p !=c:
            return p
    return participant[-1]

print(solution(['a','b','c','d'], ['a','c','d']))
print(solution2(['a','b','c','d'], ['a','c','d']))
print(solution_hash(['a','b','c','d'], ['a','c','d']))
print(solution3(['a','b','c','d'], ['a','c','d']))