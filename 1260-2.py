# DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited.append(v)
    print(v, end=" ")

    for i in range(len(graph[v])):
        if graph[v][i] == 1 and i not in visited:
            dfs(graph, i, visited)

def bfs(graph, v):
    queue = [v]
    visited = []

    while(len(queue) > 0):
        cur_v = queue.pop(0)
        visited.append(cur_v)
        print(cur_v, end=" ")

        for i in range(len(graph[cur_v])):
            if graph[cur_v][i] == 1 and i not in visited and i not in queue:
                queue.append(i)
    

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

dfs(graph, v, [])
print()
bfs(graph, v)
print()