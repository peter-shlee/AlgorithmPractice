# 적록색약
# https://www.acmicpc.net/problem/10026

import sys
from copy import deepcopy

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

adjacent_indices = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_valid_index(graph, r, c):
    if r < 0 or c < 0:
        return False

    if r >= len(graph):
        return False

    if c >= len(graph[r]):
        return False

    return True


def dfs(graph, r, c, color):
    graph[r][c] = 0

    for adjacent_index in adjacent_indices:
        next_r = r + adjacent_index[0]
        next_c = c + adjacent_index[1]

        if is_valid_index(graph, next_r, next_c):
            if graph[next_r][next_c] == color:
                dfs(graph, next_r, next_c, color)

    return
        

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input().strip()))

graph2 = deepcopy(graph)
for r in range(n):
    for c in range(n):
        if graph2[r][c] == "R":
            graph2[r][c] = "G"

answer1 = 0
for r in range(len(graph)):
    for c in range(len(graph[r])):
        if graph[r][c] != 0:
            answer1 += 1
            dfs(graph, r, c, graph[r][c])

answer2 = 0
for r in range(len(graph2)):
    for c in range(len(graph2[r])):
        if graph2[r][c] != 0:
            answer2 += 1
            dfs(graph2, r, c, graph2[r][c])

print(answer1, answer2)

