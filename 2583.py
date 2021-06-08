# 영역 구하기
# https://www.acmicpc.net/problem/2583

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

next_idx = ((0, 1), (0, -1), (1, 0), (-1, 0))

def dfs(board, i, j, area):
    global next_idx

    area += 1
    board[i][j] = True

    for idx in next_idx:
        next_i = i + idx[0]
        next_j = j + idx[1]
        if (0 <= next_i < len(board)) and (0 <= next_j < len(board[0])):
            if not board[next_i][next_j]:
                area = dfs(board, next_i, next_j, area)

    return area


m, n, k = map(int, input().split())

board = [[False] * n for _ in range(m)]

for _ in range(k):
    j1, i1, j2, i2 = map(int, input().split())
    for i in range(i1, i2):
        for j in range(j1, j2):
            board[i][j] = True

count = 0
areas = []
for i in range(m):
    for j in range(n):
        if not board[i][j]:
            area = dfs(board, i, j, 0)
            count += 1
            areas.append(area)

areas.sort()
print(count)
print(*areas)