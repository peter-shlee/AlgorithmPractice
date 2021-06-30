# 경로 찾기
# https://www.acmicpc.net/problem/11403

import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def dfs(graph, start_idx, current_idx, visited, answer):
    visited.append(current_idx)
    answer[start_idx][current_idx] = 1

    for j in range(len(graph[current_idx])):
        if graph[current_idx][j] == 1 and j not in visited:
            dfs(graph, start_idx, j, visited, answer)


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = [[0] * n for _ in range(n)]

for i in range(n):
    visited = []
    for j in range(n):
        if graph[i][j]:
            dfs(graph, i, j, visited, answer)

for row in answer:
    print(*row, sep=" ")