def solution(N):
    if (N**0.5)%1!=0:
        return -1
    else:
        return ((N**0.5)+1)**2