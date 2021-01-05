# coding=utf-8
import numpy as np


def solution(key, lock):
    key_size = len(key)  # 자물쇠와 열쇠의 크기가 다를 수 있으며, 자물쇠는 열쇠보다 작거나 같다.
    lock_size = len(lock)
    for _ in range(4):  # 네 번 굴려가며 서로 맞춰보기
        # 열쇠의 전체가 아닌 일부분이 자물쇠와 맞춰질 수 있으므로,
        # 열쇠에 자물쇠 크기만큼 빈 칸이 있다고 생각하고 열쇠를 키에 맞춰보는 전략
        extended_size = key_size + (2 * lock_size) - 2
        extended = np.zeros((extended_size, extended_size))
        extended[lock_size - 1: key_size + lock_size - 1, lock_size - 1: key_size + lock_size - 1] = key
        for i in range(key_size + lock_size - 1):
            for j in range(key_size + lock_size - 1):
                temp = extended[i:i + lock_size, j:j + lock_size]
                if opening(temp, lock):
                    return True
        key = roll_arr(key, key_size)  # 한바퀴 회전
    return False


def opening(key, lock):
    """ 두 배열을 이용해 자물쇠와 열쇠가 꼭 맞는지 판단 """
    for lst1, lst2 in zip(key, lock):
        for a, b in zip(lst1, lst2):
            if int(a + b) == 1:
                pass
            else:
                return False
    return True


def roll_arr(arr, size):
    """ 2차원 정사각형 배열을 시계 방향으로 한바퀴 회전 """
    rolled = np.zeros((size, size))
    for a, row in enumerate(arr):
        i = size - a - 1
        for b, num in enumerate(row):
            rolled[b, i] = num
    return rolled


# false
solution([[1, 1, 1], [0, 0, 0], [1, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]])
