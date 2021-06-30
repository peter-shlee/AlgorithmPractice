# 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

next_idx = [(1,0), (-1,0), (0,1), (0,-1)]


def is_valid_index(b, i, j):
    if i < 0 or j < 0:
        return False

    if i >= len(b[0]) or j >= len(b):
        return False

    return True


def dfs(b, i, j):
    b[j][i] = 0

    for idx in next_idx:
        next_i = i + idx[0]
        next_j = j + idx[1]
        if is_valid_index(b, next_i, next_j):
            if b[next_j][next_i] == 1:
                dfs(b, next_i, next_j)



t = int(input())
for __ in range(t):
    m, n, k = map(int, input().split())
    b = [[0] * m for _ in range(n)]

    for _ in range(k):
        i, j = map(int, input().split())
        b[j][i] = 1

    answer = 0
    for i in range(m):
        for j in range(n):
            if b[j][i] == 1:
                answer += 1
                dfs(b, i, j)
    
    print(answer)