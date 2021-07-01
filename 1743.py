# 음식물 피하기
# https://www.acmicpc.net/problem/1743

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

adjacent_indices = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def valid_index(graph, r, c):
    if r < 0 or c < 0:
        return False

    if r >= len(graph):
        return False

    if c >= len(graph[r]):
        return False

    return True

def dfs(graph, r, c, count):
    graph[r][c] = 0
    count += 1

    for adjacent_index in adjacent_indices:
        next_r = r + adjacent_index[0]
        next_c = c + adjacent_index[1]

        if valid_index(graph, next_r, next_c):
            if graph[next_r][next_c]:
                count = dfs(graph, next_r, next_c, count)

    return count




n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1

answer = 0
for r in range(len(graph)):
    for c in range(len(graph[r])):
        if graph[r][c] == 1:
            answer = max(dfs(graph, r, c, 0), answer)

print(answer)
