import sys


def max_volume(n, s, m, volume):
    # list로 하면 메모리 초과
    now_volume = set() | {s}
    next_volume = set()

    # 다 더하기만 해도 m을 안 넘으면 그냥 리턴
    if sum(volume) + s <= m:
        return sum(volume) + s

    # n곡까지 연주하냐/안하냐로 구분하여 탐색
    for i in range(n):
        if not now_volume:
            return -1

        while now_volume:
            now = now_volume.pop()
            if 0 <= now + volume[i] <= m:
                next_volume.add(now + volume[i])
            if 0 <= now - volume[i] <= m:
                next_volume.add(now - volume[i])

        now_volume = next_volume
        next_volume = set()

    return max(now_volume) if now_volume else -1


N, S, M = map(int, input().split())
Volume = list(map(int, sys.stdin.readline().split()))

print(max_volume(N, S, M, Volume))
