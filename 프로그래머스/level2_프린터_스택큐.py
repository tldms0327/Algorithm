def solution(prior, location):
    answer=1
    while True:
        if prior[location] >= max(prior):
            return answer+len([x for x in prior[:location] if x==prior[location]])
            break
        temp = prior.pop(0)

        if temp <max(prior):
            prior.append(temp)
        else:
            answer+=1

        if location>=1:
            location-=1
        else:
            location=len(prior)-1

    return answer
