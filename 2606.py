# 바이러스
# https://www.acmicpc.net/problem/2606

def dfs(graph, infected, current_node):
    infected[current_node] = True

    for next_node in graph[current_node]:
        if infected[next_node] == False:
            dfs(graph, infected, next_node)


num_of_computers = int(input())
num_of_edges = int(input())

infected = [False] * (num_of_computers + 1)

graph = [[]]
for _ in range(num_of_computers):
    graph.append([])

for _ in range(num_of_edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, infected, 1)
print(infected.count(True) - 1)