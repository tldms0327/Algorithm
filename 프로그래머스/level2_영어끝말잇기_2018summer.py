def solution(n, words):
	answer = [0,0]

	for i, word in enumerate(words):
		if i==0:
			continue
		else:
			if words[i-1][-1] != word[0] or word in words[:i]:
				answer = [i%n+1, 1 + i//n]
				break
	return answer

print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'bot', 'tank']))
print(solution(2, ['land', 'dream', 'mom', 'mom', 'ror']))
print(solution(3, ['land', 'dream', 'he']))