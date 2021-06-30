# https://www.acmicpc.net/problem/3987
# 보이저 1호

import sys

def can_go(space, y, x):
    if y < 0 or x < 0:
        return False

    if len(space) <= y or len(space[0]) <= x:
        return False

    if space[y][x] == "C":
        return False

    return True

up = 1
down = 2
left = 3
right = 4

def dfs(space, y, x, depth, prev_direction):
    global answer

    if space[y][x] == "C":
        return

    if prev_direction in visited[y][x]:
        answer = 987654321
        return

    visited[y][x].append(prev_direction)

    if answer < depth:
        answer = depth

    if space[y][x] == "/":
        if prev_direction == up: # go right
            if can_go(space, y, x + 1):
                dfs(space, y, x + 1, depth + 1, right)
        elif prev_direction == down: # go left
            if can_go(space, y, x - 1):
                dfs(space, y, x - 1, depth + 1, left)
        elif prev_direction == left: # go down
            if can_go(space, y + 1, x):
                dfs(space, y + 1, x, depth + 1, down)
        else: # go up
            if can_go(space, y - 1, x):
                dfs(space, y - 1, x, depth + 1, up)

    elif space[y][x] == "\\":
        if prev_direction == up: # go left
            if can_go(space, y, x - 1):
                dfs(space, y, x - 1, depth + 1, left)
        elif prev_direction == down: # go right
            if can_go(space, y, x + 1):
                dfs(space, y, x + 1, depth + 1, right)
        elif prev_direction == left: # go up
            if can_go(space, y - 1, x):
                dfs(space, y - 1, x, depth + 1, up)
        else: # go down
            if can_go(space, y + 1, x):
                dfs(space, y + 1, x, depth + 1, down)

    else:
        if prev_direction == up: # go up
            if can_go(space, y - 1, x):
                dfs(space, y - 1, x, depth + 1, up)
        elif prev_direction == down: # go down
            if can_go(space, y + 1, x):
                dfs(space, y + 1, x, depth + 1, down)
        elif prev_direction == left: # go left
            if can_go(space, y, x - 1):
                dfs(space, y, x - 1, depth + 1, left)
        else: # go right
            if can_go(space, y, x + 1):
                dfs(space, y, x + 1, depth + 1, right)

def init_visited(visited):
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            visited[i][j].clear()

sys.setrecursionlimit(10**6)
n, m = list(map(int, input().split()))
space = []
visited = []
answer = 0

for i in range(n):
    space.append(input())
    visited.append([list() for x in range(m)])


start_y, start_x = list(map(int, input().split()))
start_x -= 1 
start_y -= 1 

distance = [0] * 5

answer = 0
init_visited(visited)
dfs(space, start_y, start_x, 1, up)
distance[up] = answer

answer = 0
init_visited(visited)
dfs(space, start_y, start_x, 1, down)
distance[down] = answer

answer = 0
init_visited(visited)
dfs(space, start_y, start_x, 1, left)
distance[left] = answer

answer = 0
init_visited(visited)
dfs(space, start_y, start_x, 1, right)
distance[right] = answer

answer = max(distance)

if answer == distance[up]:
    print("U")
elif answer == distance[right]:
    print("R")
elif answer == distance[down]:
    print("D")
else:
    print("L")
if answer == 987654321:
    print("Voyager")
else:
    print(answer)