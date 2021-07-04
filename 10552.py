# DOM
# https://www.acmicpc.net/problem/10552

import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, p = map(int, input().split())

favorites = []
hates = defaultdict(lambda: -1)
visited = [-1] * (m + 1)

for i in range(n):
    f, h = map(int, input().split())
    favorites.append(f)
    if hates[h] == -1:
        hates[h] = i

current = p
count = 0
while(True):
    if visited[current] != -1:
        count = -1
        break
    visited[current] = 1

    i = hates[current]
    if i == -1:
        break

    count += 1
    current = favorites[i]

print(count)
