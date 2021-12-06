# (100+1+ | 01)+ 패턴찾기

def solution(arr):
    status = -1  # 100+1+ 패턴에서 1의 개수를 기록
    i = 0
    while i < len(arr):
        # 패턴의 시작일 때, 01이나 100으로 시작해야만 'yes'
        if status < 0:
            if arr[i:].startswith('01'):
                i += 2
            elif arr[i:].startswith('100'):
                i += 3
                status = 0
            else:
                return 'NO'
        # 100 진행중
        else:
            # 1000..이후에 1이 등장했을 때 1의 개수만 추가해준다
            if arr[i] == '1':
                status += 1
                i += 1

            # 100+1+ 이후 0이 등장했을 때
            else:
                # 1이 2개 이상이었다면 정상 패턴이 완료된 것
                if status > 1:
                    status = -1
                    if arr[i:].startswith('01'):
                        i += 2
                    else:
                        i -= 1
                # 100+1로 끝났다면 다음 패턴이 01일때만 'yes'
                elif status == 1:
                    if arr[i:].startswith('01'):
                        status = -1
                        i += 2
                    else:
                        return 'NO'
                else:
                    i += 1

    return 'YES' if status != 0 else 'NO'


answers = []
n = int(input())
for _ in range(n):
    answers.append(solution(input()))

print('\n'.join(answers))
