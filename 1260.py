# DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys


def dfs(graph, visited, current_node):
    visited[current_node] = True
    print(current_node, end=" ")

    for next_node in graph[current_node]:
        if not visited[next_node]:
            dfs(graph, visited, next_node)


def bfs(graph, start_node):
    bfs_queue = []
    visited = [False] * (len(graph) + 1)
    bfs_queue.append(start_node)
    visited[start_node] = True

    while len(bfs_queue) > 0:
        current_node = bfs_queue.pop(0)

        print(current_node, end=" ")

        for next_node in graph[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                bfs_queue.append(next_node)


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for subgraph in graph:
    subgraph.sort()

dfs(graph, visited, current_node=v)
print()
bfs(graph, start_node=v)
print()