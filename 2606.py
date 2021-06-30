# 바이러스
# https://www.acmicpc.net/problem/2606

def dfs(graph, visited, current_node):
    visited[current_node] = True

    for next_node in graph[current_node]:
        if visited[next_node] == False:
            dfs(graph, visited, next_node)


num_of_nodes = int(input())
num_of_edges = int(input())

visited = [False] * (num_of_nodes + 1)

graph = [[]]
for _ in range(num_of_nodes):
    graph.append([])

for _ in range(num_of_edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, visited, 1)
print(visited.count(True) - 1)