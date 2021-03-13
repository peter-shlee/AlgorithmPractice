# https://www.acmicpc.net/problem/17204
# 죽음의 게임

n, m = list(map(int, input().split()))

points = [0] * n
visited = [False] * n

for i in range(n):
    points[i] = int(input())

prev = 0
visited[0] = True
next = points[0]
answer = 0
while not visited[next]:
    answer += 1
    if next == m:
        break
    visited[next] = True
    next = points[next]

if visited[next]:
    answer = -1
print(answer)