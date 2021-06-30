# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(graph, visited, cur):
    visited[cur] = 1
    for i in range(len(graph[cur])):
        if graph[cur][i] and not visited[i]:
            dfs(graph, visited, i)


n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
visited = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = 1
    graph[v][u] = 1

answer = 0
for i in range(n):
    if visited[i] == 0:
        answer += 1
        dfs(graph, visited, i)

print(answer)
