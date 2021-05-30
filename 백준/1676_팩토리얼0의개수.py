n = int(input())

answer = 0
# n 보다 작은 5의 배수들에서 5로 나눠지는 개수 세기
for i in range(5 * (n//5), 0, -5):
    while i % 5 == 0:
        answer += 1
        i = i/5
print(answer)