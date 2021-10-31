import sys

read = sys.stdin.readline
n, m = map(int, read().split())
# alphabets = dict()
# for i, x in enumerate('abcdefghijklmnopqrstuvwxyz'):
#     alphabets[x] = i
known = (1 << 26) - 1
words = [0 for _ in range(n)]

for i in range(n):
    word = read().strip()
    for w in word:
        words[i] |= 1 << ord(w) - 97

for _ in range(m):
    query, letter = read().split()
    answer = 0
    idx = ord(letter) - 97
    if query == '1':
        known &= ~(1 << idx)
    else:
        known |= (1 << idx)
    for word in words:
        if word & known == word:
            answer += 1
    print(answer)
