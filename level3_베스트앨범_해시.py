def solution(genres, plays):
	music = {}
	genre = {}
	answer = []
	for i, play in enumerate(plays):
		music[i] = play
		if genres[i] not in genre:
			genre[genres[i]] = plays[i]
		else:
			genre[genres[i]] += plays[i]
	genre_sort = sorted(genre, key = lambda x: genre[x], reverse=True)
	print(music)
	print(genre)
	print(genre_sort)
	for g in genre:
		temp = music[g]
		temp = sorted(temp, key = lambda x: temp[x], reverse=True)
		answer.append(temp.keys())




	
	return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],[2500,600,150,800,500]	))



