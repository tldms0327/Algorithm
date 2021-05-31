def solution(phone_book):
	length=set(sorted([len(x) for x in phone_book]))
	
	for i in list(length):
		for pre in phone_book:
			if len(pre)==i:
				for nums in phone_book:
					if nums[0:i] == pre and nums != pre:
						return False

	return True

# 더 간단한 풀이
def solution2(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

#Trie를 이용할 수 있다! 해시문제인 이유


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
phonebook=["12", "123", "1235", "567", "88"]
for p1, p2 in zip([1,2,3,4,5],[2,3,4,5]):
	print(p1,p2)