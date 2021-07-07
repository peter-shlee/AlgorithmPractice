# 나이트의 이동
# https://www.acmicpc.net/problem/7562

# pypy3 -> 통과
# python3 -> 시간초과

import sys
from collections import deque

input = sys.stdin.readline
adjacent_indices = ((-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))


def is_valid_index(board, r, c):
    if r < 0 or c < 0:
        return False

    if len(board) <= r:
        return False

    if len(board[r]) <= c:
        return False

    return True

t = int(input())

for _ in range(t):
    l = int(input())
    s_c, s_r = map(int, input().split())
    d_c, d_r = map(int, input().split())

    if s_c == d_c and s_r == d_r:
        print(0)
        continue

    board = [[0] * l for __ in range(l)]
    board[s_r][s_c] = 1

    answer = 0
    queue = deque()
    queue.append((s_r, s_c, 0))

    while len(queue) > 0:
        cur_r, cur_c, cur_count = queue.popleft()

        for adjacent_index in adjacent_indices:
            next_r = cur_r + adjacent_index[0]
            next_c = cur_c + adjacent_index[1]

            if is_valid_index(board, next_r, next_c):
                if board[next_r][next_c] == 0:
                    if next_r == d_r and next_c == d_c:
                        answer = cur_count + 1
                        queue = []
                        break

                    board[next_r][next_c] = 1
                    queue.append((next_r, next_c, cur_count + 1))

    print(answer)