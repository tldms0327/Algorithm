def solution(n,arr1,arr2):
	answer=[0]*n
	for i in range(0,n):
		answer[i]=list("#"*n)
		temp=n-1
		while temp>=0:
			if arr1[i]%2==0 and arr2[i]%2==0:
				answer[i][temp]=" "
			
			arr1[i]=arr1[i]//2
			arr2[i]=arr2[i]//2
			temp-=1

		answer[i]="".join(answer[i])

		
	return answer

print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))
print(solution(6,[46,33,33,22,31,50],[27,56,19,14,14,10]))

print(str(['a','b']))

print((10.5).isdigit())