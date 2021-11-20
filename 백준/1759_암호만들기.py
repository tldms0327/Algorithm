from itertools import combinations

l, c = map(int, input().split())
strings = input().split()
# 모음, 자음 분리
vowels = [x for x in ['a', 'e', 'i', 'o', 'u'] if x in strings]
others = [x for x in strings if x not in vowels]
answers = []

# 자음 2개 이상
for i in range(2, len(others) + 1):
    if l - i > len(vowels) or l - i < 1:
        continue
    vowel_case = list(combinations(vowels, l - i))
    other_case = list(combinations(others, i))
    for vc in vowel_case:
        for oc in other_case:
            answer = ''.join(sorted(oc + vc))
            answers.append(answer)

print('\n'.join(sorted(answers)))
