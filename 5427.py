# 불
# https://www.acmicpc.net/problem/5427

import sys
from collections import deque

input = sys.stdin.readline

adjacent_indices = ((1, 0), (-1, 0), (0, 1), (0, -1))

def is_valid_index(graph, r, c):
    if r < 0 or c < 0:
        return False

    if len(graph) <= r:
        return False

    if len(graph[r]) <= c:
        return False

    return True

t = int(input())

for _ in range(t):
    c, r = map(int, input().split())
    graph = []
    person_queue = deque()
    fire_queue = deque()
    answer = -1

    for i in range(r):
        graph.append(list(input().strip()))

    for r in range(len(graph)):
        for c in range(len(graph[r])):
            if graph[r][c] == "*":
                fire_queue.append((r, c, 0))

            if graph[r][c] == "@":
                person_queue.append((r, c, 0))

    count = 0
    while len(person_queue) > 0:
        while True:
            if len(fire_queue) > 0 and fire_queue[0][2] == count:
                cur_r, cur_c, cur_count = fire_queue.popleft()

                for adjacent_index in adjacent_indices:
                    next_r = cur_r + adjacent_index[0]
                    next_c = cur_c + adjacent_index[1]
                    next_count = cur_count + 1

                    if is_valid_index(graph, next_r, next_c):
                        if graph[next_r][next_c] == ".": # or graph[next_r][next_c] == "@":
                            graph[next_r][next_c] = "*"
                            fire_queue.append((next_r, next_c, next_count))
            else:
                break

        while True:
            if len(person_queue) > 0 and person_queue[0][2] == count:
                cur_r, cur_c, cur_count = person_queue.popleft()

                for adjacent_index in adjacent_indices:
                    next_r = cur_r + adjacent_index[0]
                    next_c = cur_c + adjacent_index[1]
                    next_count = cur_count + 1

                    if is_valid_index(graph, next_r, next_c):
                        if graph[next_r][next_c] == ".":
                            graph[next_r][next_c] = "*"
                            person_queue.append((next_r, next_c, next_count))
                    else:
                        answer = cur_count + 1
                        person_queue = []
                        break
            else:
                break
        
        count += 1

    if answer == -1:
        print("IMPOSSIBLE")
    else:
        print(answer)



