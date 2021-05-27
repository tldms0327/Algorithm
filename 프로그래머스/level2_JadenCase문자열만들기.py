def solution(s):
	# s 에 공백이 여러개일 수도 있어서 split은 못 쓸 것 같다
	s= s.lower()
	if s[0].isalpha():
		s = s[0].upper()+s[1:]
	for idx, string in enumerate(s):
		if string.isalpha() and s[idx-1]==" ":
			s = s[:idx]+s[idx].upper()+s[idx+1:]


	return s


## Use capitalize(), title() module!!