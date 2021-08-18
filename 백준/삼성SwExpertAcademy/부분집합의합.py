def solution(n, k):
    prev = [[0, n * (n + 1) // 2]]  # 0, 모든 원소의 합
    answer = 0
    if k in [0, 1, prev[0][1]]:  # 1이거나 모든 원소의 합일 때
        return 1
    if n == k == 1 or n == k == 2:
        print(n)
        return 1

    for i in range(n, 0, -1):
        next = []
        for p in prev:
            # i 를 안 더하는 경우 / i를 안 빼는 경우
            next.append(p)
            # i 를 포함 하는 경우
            # i를 포함해도 타겟에 도달하지 않을 때는 더 탐색

            if p[0] + i == k and p[1] - i == k:
                answer += 2
            elif p[0] + i == k or p[1] - i == k:
                answer += 1
            elif p[0] + i < k < p[1] - i:
                next.append([p[0] + i, p[1] - i])
        # print(i, answer, prev)
        # print(next)

        prev = next[:]

    return answer


print(solution(100,2000))
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N, K = map(int, input().split())
#     print(f"#{test_case} {solution(N, K)}")
#
