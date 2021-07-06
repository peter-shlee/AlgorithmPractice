# 탈출
# https://www.acmicpc.net/problem/3055

import sys
from collections import deque

input = sys.stdin.readline

water = 0
hedgehog = 1

adjacent_indices = ((1, 0), (-1, 0), (0, 1), (0, -1))


def is_valid_index(graph, r, c):
    if r < 0 or c < 0:
        return False

    if len(graph) <= r:
        return False

    if len(graph[r]) <= c:
        return False

    return True


r, c = map(int, input().split())

graph = []
count = [[-1] * c for _ in range(r)]

for _ in range(r):
    graph.append(list(input().strip()))

d = None
s = None
queue = deque()
for i in range(r):
    for j in range(c):
        k = graph[i][j]
        if k == "D":
            d = (i, j)
        elif k == "S":
            s = (i, j)
        elif k == "*":
            queue.append((i, j, water))

queue.append((s[0], s[1], hedgehog))
count[s[0]][s[1]] = 0

while len(queue) > 0:
    cur_r, cur_c, k = queue.popleft()

    for adjacent_index in adjacent_indices:
        next_r = cur_r + adjacent_index[0]
        next_c = cur_c + adjacent_index[1]

        if is_valid_index(graph, next_r, next_c):
            if graph[next_r][next_c] == ".":
                graph[next_r][next_c] = "*"
                if k == hedgehog:
                    count[next_r][next_c] = count[cur_r][cur_c] + 1
                queue.append((next_r, next_c, k))
            elif graph[next_r][next_c] == "D" and k == hedgehog:
                count[next_r][next_c] = count[cur_r][cur_c] + 1
                queue = []
                break

if count[d[0]][d[1]] == -1:
    print("KAKTUS")
else:
    print(count[d[0]][d[1]])
