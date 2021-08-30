# silver 1
N = int(input())
L = list(map(int, input().split()))
answer = []


def back_tracking(energy_sum, lst):
    # 구슬이 두 개면 이때까지 모은 energy 합을 answer에 저장
    if len(lst) == 2:
        answer.append(energy_sum)

    # 모든 경우의 수 다 찾아보기
    for i in range(1, len(lst) - 1):
        temp = lst[i - 1] * lst[i + 1]
        deleted_energy = lst[i]
        del lst[i]
        back_tracking(energy_sum + temp, lst)
        lst.insert(i, deleted_energy)
    return energy_sum


back_tracking(0, L)
print(max(answer))
