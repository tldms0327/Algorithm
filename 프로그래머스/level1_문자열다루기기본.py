def solution(s):
	try:
		num= int(s)
		return len(s)==4 or len(s)==6
	except:
		return False

#다른사람 풀이: isdigit()이용!
def alpha_string(s):
	return s.isdigit() and len(s) in (4,6)