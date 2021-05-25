def solution(arr):
    arr.remove(min(arr))
    if not arr:
        return [-1]
    return arr

print(solution([-10]))
print(solution([1,8,6,5,7,2,9,12,58,10]))