# 탈출
# https://www.acmicpc.net/problem/16397

import sys
from collections import deque

input = sys.stdin.readline

n, t, g = map(int, input().split())

queue = deque()
queue.append(n)
visited = [-1] * (10**5 + 1)
visited[n] = 0

while len(queue) > 0:
    c = queue.popleft()

    if visited[c] == t:
        break

    if c + 1 <= 99999:
        if visited[c + 1] == -1:
            visited[c + 1] = visited[c] + 1
            queue.append(c + 1)

    if c * 2 <= 99999:
        nc = list(map(int, list(str(c * 2))))
        nc[0] -= 1
        nc = list(map(str, nc))
        nc = int("".join(nc))

        if nc >= 0:
            if visited[nc] == -1:
                visited[nc] = visited[c] + 1
                queue.append(nc)

if visited[g] == -1:
    print("ANG")
else:
    print(visited[g])
