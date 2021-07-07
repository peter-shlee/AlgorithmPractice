# 토마토
# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

input = sys.stdin.readline
adjacent_indices = ((1, 0), (-1, 0), (0, 1), (0, -1))


def is_valid_index(board, r, c):
    if r < 0 or c < 0:
        return False

    if len(board) <= r:
        return False

    if len(board[r]) <= c:
        return False

    return True


c, r = map(int, input().split())

board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

answer = 0
queue = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == 1:
            queue.append((i, j, 0))

while len(queue) > 0:
    cur_r, cur_c, cur_count = queue.popleft()
    answer = cur_count

    for adjacent_index in adjacent_indices:
        next_r = cur_r + adjacent_index[0]
        next_c = cur_c + adjacent_index[1]

        if is_valid_index(board, next_r, next_c):
            if board[next_r][next_c] == 0:
                board[next_r][next_c] = 1
                queue.append((next_r, next_c, cur_count + 1))


for i in range(r):
    for j in range(c):
        if board[i][j] == 0:
            answer = -1

print(answer)