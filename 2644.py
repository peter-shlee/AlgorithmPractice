# 촌수계산
# https://www.acmicpc.net/problem/2644

import sys

input = sys.stdin.readline

n = int(input())
s, e = map(int, input().split())
m = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    p, c = map(int, input().split())
    graph[p][c] = 1
    graph[c][p] = 1

queue = [(s, 0)]
visited = []
answer = -1
while len(queue) > 0:
    cur, count = queue.pop(0)

    for i in range(len(graph[cur])):
        if graph[cur][i] == 1:
            if i not in visited:
                if i == e:
                    answer = count + 1
                    break
                else:
                    visited.append(i)
                    queue.append((i, count + 1))

print(answer)