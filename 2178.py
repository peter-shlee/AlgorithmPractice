# 미로 탐색
# https://www.acmicpc.net/problem/2178

import sys

input = sys.stdin.readline


def is_valid_index(graph, r, c):
    if r < 0 or c < 0:
        return False

    if len(graph) <= r:
        return False

    if len(graph[r]) <= c:
        return False

    return True


n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, list(input().strip()))))

adjacent_indices = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = [(0, 0, 1)]
graph[0][0] = 0
answer = -1
break_flag = False
while len(queue) > 0 and not break_flag:
    cur_r, cur_c, count = queue.pop(0)

    for adjacent_index in adjacent_indices:
        next_r = cur_r + adjacent_index[0]
        next_c = cur_c + adjacent_index[1]

        if is_valid_index(graph, next_r, next_c):
            if graph[next_r][next_c] == 1:

                if next_r == n - 1 and next_c == m - 1:
                    answer = count + 1
                    break_flag = True
                    break

                graph[next_r][next_c] = 0
                queue.append((next_r, next_c, count + 1))

print(answer)