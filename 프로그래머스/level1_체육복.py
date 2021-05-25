def solution(n, lost, reserve):
	a=lost[:]
	for i in lost:
		if i in reserve:
			a.remove(i)
			reserve.remove(i)
	lost=a[:]
	for i in lost:
		if(i-1) in reserve:
			a.remove(i)
			reserve.remove(i-1)
		elif (i+1) in reserve:
			a.remove(i)
			reserve.remove(i+1)
	return n-len(a)

# 다른 사람 풀이
def solution2(n, lost, reserve):
	# pythonic code...빨리 익히자ㅠ 
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)



print(solution2(5,[2,4], [1,3,5]))
print(solution2(5,[2,4], [3]))
print(solution(10,[1,6,7,9], [2,6,7,8]))
a=input('a:')
b=input('b:')
print(a+b)