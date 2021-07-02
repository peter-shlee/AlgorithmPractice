# 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys

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


def dfs(graph, r, c, count):
    graph[r][c] = 0
    count += 1

    for adjacent_index in adjacent_indices:
        next_r = r + adjacent_index[0]
        next_c = c + adjacent_index[1]

        if is_valid_index(graph, next_r, next_c):
            if graph[next_r][next_c]:
                count = dfs(graph, next_r, next_c, count)

    return count


n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, list(input().strip()))))

counts = []
answer = 0
for r in range(n):
    for c in range(n):
        if graph[r][c]:
            answer += 1
            counts.append(dfs(graph, r, c, 0))

counts.sort()

print(answer)
print(*counts, sep="\n")