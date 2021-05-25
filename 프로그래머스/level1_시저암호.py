def solution(s,n):
	big='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
	small='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
	# b, s = dict(), dict()
	# for i in range(1,27):
	# 	b[i], s[i] = big[i-1], small[i-1]
	answer=''

	for letter in s:

		if letter in big:
			for idx, l in enumerate(big):
				if l==letter:
					try: 
						answer+=big[idx+n]
					except: 
						answer+=big[idx+n-26]
		elif letter in small:
			for idx, l in enumerate(small):
				if l==letter:
					try: 
						answer+=small[idx+n]
					except: 
						answer+=small[idx+n-26]
		else:
			answer+=' '

#아스키코드를 써먹자...
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)


	return answer

print(solution("AB",1))
print(solution("z", 25))
print(solution("a B z",4))
print(solution("z Z  s  f", 2))



