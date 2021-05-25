def solution(x):
    a=[int(i) for i in str(x)]
    if x%sum(a)==0:
        return True
    else:
        return False
x=123
a=[int(i) for i in str(x)]
print(sum(a))

print(solution(10))